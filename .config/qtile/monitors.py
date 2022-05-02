from Xlib import display as xdisplay


def get_num_monitors():
    num_monitors = 0
    try:
        display = xdisplay.Display()
        screen = display.screen()
        resources = screen.root.xrandr_get_screen_resources()

        for output in resources.outputs:
            monitor = display.xrandr_get_output_info(
                output, resources.config_timestamp
            )
            preferred = False
            if hasattr(monitor, "preferred"):
                preferred = monitor.preferred
            elif hasattr(monitor, "num_preferred"):
                preferred = monitor.num_preferred

            if preferred:
                num_monitors += 1
    except Exception:
        # always setup at least one monitor
        return 1
    else:
        return num_monitors
