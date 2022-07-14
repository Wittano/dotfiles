import abc
import enum


class Colors:

    def __init__(self, border="", background="", text=""):
        self.border = border
        self.background = background
        self.text = text


class Bar:
    def __init__(self,
                 background: str = "",
                 foreground: str = "",
                 separator_color: str = "",
                 focused_workspace: Colors = Colors(),
                 active_workspace: Colors = Colors(),
                 inactive_workspace: Colors = Colors(),
                 urgent_workspace: Colors = Colors(),
                 first_widget: Colors = Colors(),
                 second_widget: Colors = Colors()):
        self.second_widget = second_widget
        self.first_widget = first_widget
        self.foreground = foreground
        self.background = background
        self.separator_color = separator_color
        self.focused_workspace = focused_workspace
        self.active_workspace = active_workspace
        self.inactive_workspace = inactive_workspace
        self.urgent_workspace = urgent_workspace


class Theme(abc.ABC):
    border_focus = ""
    border_normal = ""
    active_border = ""
    window_name = ""
    bar = Bar()


class PolybarTheme:
    background = "#212337"
    background_alt = "#444"
    foreground = "#c8d3f5"
    foreground_alt = "#555"
    selected = "#C3E88D"
    selected_workspace = Colors(text="#86e1fc")
    active_workspace = Colors(text="#b1e16a")
    title_app = "#55cc80"
    border = "#212337"
    kernel = "#ff995e"
    cpu = "#ff98a4"
    network = "#c3e88d"
    time = "#50c4fa"
    volume = "#677CE4"
    free_space = "#CC75BC"
    empty_workspace = "#555"


class MyTheme(Theme):
    border_normal = "#212337"
    border_focus = "#86e1fc"
    active_border = "#bd93f9"
    window_name = "#55cc80"

    bar = Bar(
        background="#212337",
        foreground="#c8d3f5",
        separator_color="#555",
        focused_workspace=Colors(border="#212337", background="#212337", text="#86e1fc"),
        active_workspace=Colors(border="#212337", background="#212337", text="#b1e16a"),
        inactive_workspace=Colors(border="#282A36", background="#212337", text="#c8d3f5"),
        urgent_workspace=Colors(border="#212337", background="#212337", text="#ff995e"),
        first_widget=Colors(border="#212337", background="#4da561", text="#F8F8F2"),
        second_widget=Colors(border="#212337", background="#677CE4", text="#F8F8F2"),
    )


_DRACULA_COLORS = {
    "background": "#282a36",
    "current_line": "#44475a",
    "selection": "#44475a",
    "foreground": "#f8f8f2",
    "comment": "#6272a4",
    "cyan": "#8be9fd",
    "green": "#50fa7b",
    "orange": "#ffb86c",
    "pink": "#ff79c6",
    "purple": "#bd93f9",
    "red": "#ff5555",
    "yellow": "#f1fa8c"
}


class DraculaTheme(Theme):
    border_normal = _DRACULA_COLORS["selection"]
    border_focus = _DRACULA_COLORS["purple"]
    active_border = _DRACULA_COLORS["pink"]
    window_name = _DRACULA_COLORS["green"]

    bar = Bar(
        background=_DRACULA_COLORS["background"],
        foreground=_DRACULA_COLORS["foreground"],
        separator_color=_DRACULA_COLORS["current_line"],
        focused_workspace=Colors(border=_DRACULA_COLORS["comment"], background=_DRACULA_COLORS["comment"],
                                 text=_DRACULA_COLORS["foreground"]),
        active_workspace=Colors(border=_DRACULA_COLORS["selection"], background=_DRACULA_COLORS["selection"],
                                text=_DRACULA_COLORS["foreground"]),
        inactive_workspace=Colors(border=_DRACULA_COLORS["background"], background=_DRACULA_COLORS["background"],
                                  text="#BFBFBF"),
        urgent_workspace=Colors(border=_DRACULA_COLORS["selection"], background=_DRACULA_COLORS["red"],
                                text=_DRACULA_COLORS["foreground"]),
        first_widget=Colors(border=_DRACULA_COLORS["selection"], background=_DRACULA_COLORS["comment"],
                            text=_DRACULA_COLORS["foreground"]),
        second_widget=Colors(border=_DRACULA_COLORS["selection"], background=_DRACULA_COLORS["selection"],
                             text=_DRACULA_COLORS["foreground"])
    )
