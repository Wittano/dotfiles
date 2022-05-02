import platform
from typing import List

from libqtile import bar, layout, widget
from libqtile.config import Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from monitors import get_num_monitors
from themes import MyTheme
from widgets import create_powerline_sep

mod = "mod4"
terminal = guess_terminal()

theme = MyTheme()

layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": theme.border_focus,
    "border_normal": theme.border_normal
}

keys: List[Key] = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "mod1"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "mod1"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc="Put the focused window to/from fullscreen mode"),

    Key([mod], "t", lazy.window.toggle_floating(),
        desc="Put the focused window to/from floating mode"),

    Key([mod, "shift"], "p", lazy.spawn("flameshot gui"),
        desc="Make screenshot"),

    Key([mod], "d", lazy.spawn("rofi -show drun"),
        desc="Run rofi in dmenu mode"),

    Key([mod], "m", lazy.spawn("amixer sset Master toggle"),
        desc="Toggle mute/unmute volume"),

    Key([mod], "p", lazy.spawn("amixer sset Master 1%"),
        desc="Increases volume"),

    Key([mod], "o", lazy.spawn("amixer sset Master 1%-"),
        desc="Decreases volume")
]

groups: List[Group] = [
    Group(name="1", label="dev"),
    Group(name="2", label="www"),
    Group(name="3", label="sys", layout="MonadTall"),
    Group(name="4", label="doc"),
    Group(name="5", label="virt"),
    Group(name="6", label="game", layout="max"),
    Group(name="7", label="chat", layout="max"),
    Group(name="8", label="www"),
]

for group in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], group.name, lazy.group[group.name].toscreen(),
            desc=f"Switch to group {group.name}"),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], group.name, lazy.window.togroup(group.name, switch_group=True),
            desc=f"Switch to & move focused window to group {group.name}"),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    # layout.Columns(
    #     border_on_single=True,
    #     border_normal_stack=themes[active_theme]["border_normal"],
    #     border_focus_stack=themes[active_theme]["border_focus"],
    #     **layout_theme
    # ),
    layout.Max(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        change_ratio=0.2,
        **layout_theme
    ),
    layout.MonadWide(**layout_theme),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(
        panel_width=200,
        margin_y=10,
        active_bg=theme.active_border,
        inactive_bg=theme.border_normal,
        **layout_theme
    ),
    # layout.VerticalTile(),
    # layout.Zoomy(),
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

textbox_config = dict(
    fontsize=14,
    padding=10
)

separator = widget.TextBox(
    text='|',
    background=theme.bar.background,
    foreground=theme.bar.foreground,
)

first_powerline_sep = create_powerline_sep(theme.bar.first_widget)
second_powerline_sep = create_powerline_sep(theme.bar.second_widget)

widgets = [
    widget.TextBox(
        text='',
        fontsize=24,
        background=theme.bar.background,
        foreground=theme.bar.foreground,
        padding=2,
        mouse_callbacks={
            "Button1": lazy.spawn(terminal)
        }
    ),
    widget.CurrentLayout(
        padding=5,
    ),
    separator,
    widget.GroupBox(
        highlight_method='line',
        borderwidth=3,
        this_current_screen_border=theme.bar.focused_workspace.text,
        block_highlight_text_color=theme.bar.focused_workspace.text,
        active=theme.bar.active_workspace.text,
        foreground=theme.bar.inactive_workspace.text,
        inactive=theme.bar.inactive_workspace.text,
        urgent_text=theme.bar.urgent_workspace.text,
        urgent_border=theme.bar.urgent_workspace.background,
        urgent_alert_method='block',
        invert_mouse_wheel=True,
    ),
    separator,
    widget.WindowName(
        foreground=theme.window_name,
        max_chars=30,
    ),
    *first_powerline_sep,
    widget.TextBox(
        text=f"{platform.system()} {platform.release()}",
        background=theme.bar.first_widget.background,
        foreground=theme.bar.first_widget.text,
        **textbox_config
    ),
    *second_powerline_sep,
    widget.Volume(
        fmt='Vol: {}',
        background=theme.bar.second_widget.background,
        foreground=theme.bar.second_widget.text,
        **textbox_config
    ),
    widget.CPU(
        background=theme.bar.first_widget.background,
        foreground=theme.bar.first_widget.text,
        **textbox_config
    ),
    widget.Net(
        interface="eno1",
        background=theme.bar.second_widget.background,
        foreground=theme.bar.second_widget.text,
        **textbox_config
    ),
    widget.CheckUpdates(
        update_interval=1800,
        distro="Arch_checkupdates",
        colour_have_updates=theme.bar.first_widget.text,
        colour_no_updates=theme.bar.first_widget.text,
        mouse_callbacks={
            'Button1': lambda: lazy.spawn(f'{terminal} -e sudo pacman -Syu')
        },
        background=theme.bar.first_widget.background,
        foreground=theme.bar.first_widget.text,
        **textbox_config
    ),
    widget.Clock(
        format='%Y-%m-%d %a %I:%M %p',
        background=theme.bar.second_widget.background,
        foreground=theme.bar.second_widget.text,
        **textbox_config
    ),
    widget.Systray(
        background=theme.bar.first_widget.background,
        foreground=theme.bar.first_widget.text,
        **textbox_config
    )
]

screens = [
    Screen(
        top=bar.Bar(
            widgets,
            32,
            background=theme.bar.background,
            border_color=theme.bar.background
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    )
    # ) for i in range(get_num_monitors())
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])

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
