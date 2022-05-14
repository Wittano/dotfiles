from typing import Tuple

from libqtile import widget
from libqtile.widget.sep import Sep
from libqtile.widget.textbox import TextBox

from themes import Colors, Bar


def _get_first_color_background(color: Colors | Bar) -> str:
    if isinstance(color, Colors):
        return color.background
    else:
        return color.first_widget.background


def create_powerline_sep(first_color: Colors | Bar, second_color: Colors = None) -> Tuple[TextBox, Sep]:
    return (
        widget.TextBox(
            text=u"\ue0b2",
            font="Powerline",
            foreground=_get_first_color_background(first_color),
            background=second_color.background if second_color is not None else first_color.background,
            fontsize=25,
            padding=0
        ),
        widget.Sep(padding=3, linewidth=0, background=_get_first_color_background(first_color)),
    )
