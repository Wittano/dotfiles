import abc


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


class DraculaTheme(Theme):
    border_normal = "#44475a"
    border_focus = "#bd93f9"
    active_border = "#ff79c6"
    window_name = "#FF5555"

    bar = Bar(
        background="#212337",
        foreground="#c8d3f5",
        separator_color="#555",
        focused_workspace=Colors(border="#6272A4", background="#6272A4", text="#F8F8F2"),
        active_workspace=Colors(border="#44475A", background="#44475A", text="#F8F8F2"),
        inactive_workspace=Colors(border="#282A36", background="#282A36", text="#BFBFBF"),
        urgent_workspace=Colors(border="#44475A", background="#FF5555", text="#F8F8F2"),
        first_widget=Colors(border="#44475A", background="#6272A4", text="#F8F8F2"),
        second_widget=Colors(border="#44475A", background="#44475A", text="#F8F8F2")
    )
