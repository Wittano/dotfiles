import platform
from typing import Tuple, List, Optional

from libqtile import widget, bar
from libqtile.command import lazy
from libqtile.config import Screen
from libqtile.widget.sep import Sep
from libqtile.widget.textbox import TextBox

from monitors import get_monitors
from themes import Colors, Bar, Theme

_textbox_config = dict(
    fontsize=14,
    padding=10
)


class ScreenCreator:

    def __init__(self, theme: Theme, terminal: str = "terminator"):
        self.__theme = theme
        self.__terminal_name = terminal
        self.__info_powerline_sep = self.__create_powerline_sep(theme.bar)
        self.__info_powerline_sep_alt = self.__create_powerline_sep(theme.bar, use_second_widget_color=True)
        self.__first_powerline_sep = self.__create_powerline_sep(theme.bar.first_widget, theme.bar.second_widget)
        self.__second_powerline_sep = self.__create_powerline_sep(theme.bar.second_widget, theme.bar.first_widget)

    @staticmethod
    def __get_first_color_background(color: Colors | Bar, use_second_widget_color: Optional[bool] = False) -> str:
        if isinstance(color, Colors):
            return color.background
        elif use_second_widget_color:
            return color.second_widget.background
        else:
            return color.first_widget.background

    def __create_powerline_sep(self,
                               first_color: Colors | Bar,
                               second_color: Optional[Colors] = None,
                               use_second_widget_color: Optional[bool] = False) -> Tuple[TextBox, Sep]:

        return (
            widget.TextBox(
                text=u"\ue0b2",
                font="Powerline",
                foreground=self.__get_first_color_background(first_color,
                                                             use_second_widget_color=use_second_widget_color),
                background=second_color.background if second_color is not None else first_color.background,
                fontsize=25,
                padding=0
            ),
            widget.Sep(
                padding=3,
                linewidth=0,
                background=self.__get_first_color_background(first_color,
                                                             use_second_widget_color=use_second_widget_color)),
        )

    def __get_navigation_bar_part(self) -> List[TextBox]:
        """
        Get left part of status bar
        :return:
        """

        separator = SeparatorWidget(self.__theme)

        return [
            LogoWidget(self.__theme, self.__terminal_name),
            CurrentLayoutWidget(),
            separator,
            GroupBoxWidget(self.__theme),
            separator,
            TitlebarWidget(self.__theme),
        ]

    def __get_central_bar_part(self):

        return [
            *self.__info_powerline_sep,
            KernelWidget(self.__theme),
            *self.__second_powerline_sep,
            VolumeWidget(self.__theme),
            *self.__first_powerline_sep,
            CPUWidget(self.__theme),
            *self.__second_powerline_sep,
            NetWidget(self.__theme),
            *self.__first_powerline_sep,
            CheckUpdatesWidget(self.__theme, self.__terminal_name),
        ]

    def __get_right_bar_part(self, is_primary: bool = True):
        is_only_one_monitor: bool = is_primary and get_monitors() == 1
        is_minor_monitor: bool = not is_primary and get_monitors() > 1

        right_part = [
            *(self.__second_powerline_sep if is_primary else self.__info_powerline_sep_alt),
            ClockWidget(self.__theme),
        ]

        if is_only_one_monitor or is_minor_monitor:
            right_part.append(SystrayWidget(self.__theme))

        return right_part

    def create(self, is_primary: bool = True) -> Screen:
        if is_primary:
            widgets = self.__get_navigation_bar_part() + self.__get_central_bar_part() + self.__get_right_bar_part()
        else:
            widgets = self.__get_navigation_bar_part() + self.__get_right_bar_part(is_primary)

        return Screen(
            top=bar.Bar(
                widgets,
                32,
                background=self.__theme.bar.background,
                border_color=self.__theme.bar.background,
                width=1920
            )
        )


class SeparatorWidget(widget.TextBox):
    def __init__(self, theme: Theme):
        super(SeparatorWidget, self).__init__(
            text='|',
            background=theme.bar.background,
            foreground=theme.bar.foreground,
        )


class LogoWidget(widget.TextBox):
    def __init__(self, theme: Theme, terminal: str = "terminator"):
        super(LogoWidget, self).__init__(
            text='',
            fontsize=24,
            background=theme.bar.background,
            foreground=theme.bar.foreground,
            padding=5,
            mouse_callbacks={
                "Button1": lazy.spawn(terminal)
            }
        )


class TitlebarWidget(widget.WindowName):
    def __init__(self, theme: Theme):
        super(TitlebarWidget, self).__init__(
            foreground=theme.window_name,
            max_chars=30,
        )


class CurrentLayoutWidget(widget.CurrentLayout):
    def __init__(self):
        super(CurrentLayoutWidget, self).__init__(
            padding=5
        )


class GroupBoxWidget(widget.GroupBox):
    def __init__(self, theme: Theme):
        super(GroupBoxWidget, self).__init__(
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
            disable_drag=True
        )


class NetWidget(widget.Net):
    def __init__(self, theme: Theme):
        super(NetWidget, self).__init__(
            interface="eno1",
            background=theme.bar.second_widget.background,
            foreground=theme.bar.second_widget.text,
            **_textbox_config
        )


class CPUWidget(widget.CPU):
    def __init__(self, theme: Theme):
        super(CPUWidget, self).__init__(
            background=theme.bar.first_widget.background,
            foreground=theme.bar.first_widget.text,
            format='CPU {load_percent}%',
            **_textbox_config
        )


class VolumeWidget(widget.Volume):
    def __init__(self, theme: Theme):
        super(VolumeWidget, self).__init__(
            fmt='Vol: {}',
            background=theme.bar.second_widget.background,
            foreground=theme.bar.second_widget.text,
            **_textbox_config
        )


class CheckUpdatesWidget(widget.CheckUpdates):
    def __init__(self, theme: Theme, terminal: str = "terminator"):
        super(CheckUpdatesWidget, self).__init__(
            update_interval=1800,
            distro="Arch_checkupdates",
            colour_have_updates=theme.bar.first_widget.text,
            colour_no_updates=theme.bar.first_widget.text,
            mouse_callbacks={
                'Button1': lambda: lazy.spawn(f'{terminal} -e sudo pacman -Syu')
            },
            background=theme.bar.first_widget.background,
            foreground=theme.bar.first_widget.text,
            **_textbox_config
        )


class ClockWidget(widget.Clock):
    def __init__(self, theme: Theme):
        super(ClockWidget, self).__init__(
            format='%Y-%m-%d %a %I:%M %p',
            background=theme.bar.second_widget.background,
            foreground=theme.bar.second_widget.text,
            **_textbox_config
        )


class SystrayWidget(widget.Systray):
    def __init__(self, theme: Theme):
        super(SystrayWidget, self).__init__(
            background=theme.bar.background,
            foreground=theme.bar.first_widget.text,
            **_textbox_config
        )


class KernelWidget(widget.TextBox):
    def __init__(self, theme: Theme):
        super(KernelWidget, self).__init__(
            text=self.__create_kernel_version(),
            background=theme.bar.first_widget.background,
            foreground=theme.bar.first_widget.text,
            **_textbox_config
        )

    @staticmethod
    def __create_kernel_version() -> str:
        return f"{platform.system()} {platform.release()}"
