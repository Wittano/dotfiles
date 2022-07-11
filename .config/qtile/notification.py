from libqtile.core.manager import Qtile


def send_notification(qtile: Qtile, msg: str = ""):
    qtile.cmd_spawn(f"notify-send '{msg}'")
