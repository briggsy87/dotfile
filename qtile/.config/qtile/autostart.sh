#!/usr/bin/env bash
set -euo pipefail

nm-applet & 
dropbox start &

numlockx &

#picom --experimental-backends &
#dunst &
#unclutter &
#blueberry-tray &
#greenclip daemon &
#light-locker --lock-after-screensaver=0 --no-lock-on-suspend --no-lock-on-lid --no-idle-hint &
#xidlehook --not-when-fullscreen --not-when-audio --timer 423 'screensaver' '' --timer 180 'xset dpms force off; lockscreen.sh' '' &
#flashfocus &
#redshift-gtk -l 44.3894:-79.6903 &
#~/.config/eww/scripts/getweather &
#feh-blur --darken 0 -b 6 &
#eww daemon
#while true; do
#    if eww ping; then 
#        eww open border &
#        eww open border1 &
#        eww open border2 &
#        break
#    fi
#done &
