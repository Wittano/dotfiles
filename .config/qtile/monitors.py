import subprocess

import libqtile.log_utils


def get_monitors() -> int:
    """
    Get number of active and connected monitors

    :return:
        Number of monitors
    """
    try:
        monitors: list[str] = subprocess.check_output(
            args='xrandr --query | grep " connected"',
            shell=True
        ).decode().split('\n')

        return len(list(filter(lambda x: x.strip() != '', monitors)))
    except Exception as error:
        libqtile.log_utils.logger.warning(error)
        return 1
