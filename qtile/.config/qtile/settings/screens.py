# Multimonitor support

from libqtile.config import Screen
from libqtile import bar, widget
from libqtile.log_utils import logger
from settings.widgets import primary_widgets, secondary_widgets
import subprocess


def status_bar(widgets):
    return bar.Bar(widgets, 24, opacity=0.95)

def get_monitors():
    xr = subprocess.check_output('xrandr --query | grep " connected"', shell=True).decode().split('\n')
    monitors = len(xr) - 1 if len(xr) > 2 else len(xr)
    return monitors


monitors = get_monitors()

# Move window to screen with Mod, Alt and number
#for i in range(monitors):
#    keys.extend([Key([mod, "mod1"], str(i), lazy.window.toscreen(i))])

screens = []

for monitor in range(monitors):
    if monitor == 0:
        screens.append(Screen(top=status_bar(primary_widgets)))
    else:
        screens.append(Screen(top=status_bar(secondary_widgets)))

# screens = [Screen(top=status_bar(primary_widgets))]
# if monitors > 1:
#     for _ in range(1, monitors):
#         screens.append(Screen(top=status_bar(secondary_widgets)))
#         pass
