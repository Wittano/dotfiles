import os
import re
import subprocess
import threading
from typing import List

import libqtile.hook
from libqtile import layout
from libqtile.config import Drag, Group, Key, Match
from libqtile.core.manager import Qtile
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import monitors
from groups import get_default_groups
from layouts import LayoutsCollection
from monitors import get_monitors_count, map_wacom_to_one_monitor
from themes import MyTheme, DraculaTheme
from widgets import ScreenCreator

SUPER_KEY = "mod4"
ALT_KEY = "mod1"
SHIFT_KEY = "shift"
CONTROL_KEY = "control"

WEB_BROWSER = "vivaldi-stable"

QTILE: Qtile = libqtile.qtile

terminal = guess_terminal()

theme = DraculaTheme()

volume_percent_ratio = 5

WITH_BAR = False

keys: List[Key] = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Switch between windows
    Key([SUPER_KEY], "h", lazy.layout.left(), desc="Move focus to left"),

    Key([SUPER_KEY], "l", lazy.layout.right(), desc="Move focus to right"),

    Key([SUPER_KEY], "j", lazy.layout.down(), desc="Move focus down"),

    Key([SUPER_KEY], "k", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([SUPER_KEY, SHIFT_KEY], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([SUPER_KEY, SHIFT_KEY], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([SUPER_KEY, SHIFT_KEY], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([SUPER_KEY, SHIFT_KEY], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([SUPER_KEY, CONTROL_KEY], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([SUPER_KEY, CONTROL_KEY], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([SUPER_KEY, CONTROL_KEY], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([SUPER_KEY, CONTROL_KEY], "k", lazy.layout.grow_up(), desc="Grow window up"),

    Key([SUPER_KEY], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([SUPER_KEY, SHIFT_KEY], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    Key([SUPER_KEY], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([SUPER_KEY], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    Key([SUPER_KEY], "x", lazy.window.kill(), desc="Kill focused window"),

    Key([SUPER_KEY, ALT_KEY], "r", lazy.reload_config(), desc="Reload the config"),

    Key([SUPER_KEY, ALT_KEY], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    Key([SUPER_KEY], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    Key([SUPER_KEY], "f", lazy.window.toggle_fullscreen(),
        desc="Put the focused window to/from fullscreen mode"),

    Key([SUPER_KEY], "s", lazy.window.toggle_floating(),
        desc="Put the focused window to/from floating mode"),

    Key([SUPER_KEY, SHIFT_KEY], "p", lazy.spawn("flameshot gui"),
        desc="Make screenshot"),

    Key([SUPER_KEY], "d", lazy.spawn("rofi -show drun"),
        desc="Run rofi in dmenu mode"),

    Key([SUPER_KEY], "w", lazy.spawn("rofi -show window"),
        desc="""
                Run rofi in window mode - special mode, 
                that show every opened applications on each workspaces
            """),

    Key([SUPER_KEY], "m", lazy.spawn("amixer sset Master toggle"),
        desc="Toggle mute/unmute volume"),

    Key([SUPER_KEY], "p", lazy.spawn(f"amixer sset Master {volume_percent_ratio}%+"),
        desc="Increases volume"),

    Key([SUPER_KEY], "o", lazy.spawn(f"amixer sset Master {volume_percent_ratio}%-"),
        desc="Decreases volume"),

    Key([SUPER_KEY], "space", monitors.swap_monitor,
        desc="Toggle focused window between monitors"),

    Key([SUPER_KEY], "n", lazy.next_screen(),
        desc="Toggle focused screen"),

    Key([SUPER_KEY, SHIFT_KEY], "q", lazy.spawn("systemctl poweroff"), desc="Shutdown Linux"),

    Key([SUPER_KEY], "b", lazy.spawn(f"{terminal} -e btop"), desc="Launch web browser"),

    Key([SUPER_KEY], "i", lazy.spawn(f"bash {os.environ['HOME']}/.local/bin/sys-info"),
        desc="Show system info"),

    Key([SUPER_KEY], "u", lazy.spawn(f"bash {os.environ['HOME']}/.local/bin/current-time"),
        desc="Show system info")
]

groups: List[Group] = get_default_groups()

for group in groups:
    keys.extend([
        Key([SUPER_KEY], group.name, lazy.group[group.name].toscreen(),
            desc=f"Switch to group {group.name}"),

        Key([SUPER_KEY, SHIFT_KEY], group.name, lazy.window.togroup(group.name, switch_group=True),
            desc=f"Switch to & move focused window to group {group.name}"),

        Key([SUPER_KEY, CONTROL_KEY], group.name, lazy.group[group.name].toscreen(1))
    ])

layout_collection = LayoutsCollection(theme)

layouts = [
    layout_collection.max_layout,
    layout_collection.monad_tall_layout
]

widget_defaults = dict(
    font='sans',
    fontsize=14,
    padding=3,
)

extension_defaults = widget_defaults.copy()

widget_config = dict(
    font='sans',
    fontsize=14,
)

screen_creator = ScreenCreator(theme, terminal)

if WITH_BAR:
    screens = [
                  screen_creator.create()
              ] + [screen_creator.create(is_primary=False)] if get_monitors_count() > 1 else []
else:
    screens = [screen_creator.create_without_bar() for _ in range(get_monitors_count())]

# Drag floating layouts.
mouse = [
    Drag([SUPER_KEY], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([SUPER_KEY], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
]

dgroups_key_binder = None
dgroups_app_rules: List = []
follow_mouse_focus = True
bring_front_click = True
cursor_warp = True

floating_layout = layout.Floating(
    border_focus=theme.border_focus,
    border_normal=theme.border_normal,
    border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(wm_class=re.compile('[pP]inentry*')),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


def _map_wacom_output(screen_index: int = 0):
    threading.Thread(target=map_wacom_to_one_monitor, args=(screen_index,)).start()


@libqtile.hook.subscribe.startup_once
def autostart_hook():
    home_dir = os.environ['HOME']
    subprocess.call([f"{home_dir}/.config/qtile/autostart.sh"])

    _map_wacom_output()


@libqtile.hook.subscribe.current_screen_change
async def map_tablet_to_one_monitor():
    _map_wacom_output(QTILE.current_screen.index)
