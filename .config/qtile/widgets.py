from typing import Tuple

from libqtile import widget
from libqtile.widget.sep import Sep
from libqtile.widget.textbox import TextBox

from themes import Colors


def create_powerline_sep(color: Colors) -> Tuple[TextBox, Sep]:
    return (
        widget.TextBox(
            text=u"\ue0b2",
            font="Powerline",
            foreground=color.text,
            background=color.background,
            fontsize=14,
        ),
        widget.Sep(padding=5, linewidth=0, background=color.background),
    )
