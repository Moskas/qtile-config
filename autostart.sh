#!/usr/bin/env bash

#sleep 5
#setxkbmap pl & # Set keyboard layout
#xrandr --output DP-0 --mode 1920x1080 --rate '143.98' & # Monitor setup
random-wallpaper & # Set random wallpaper

# Random apps
vesktop &
nicotine &
openrgb -p Red & # Set RGB profile
mpd-notify-rs &
mpdas &
systemctl --user restart mpd-discord-rpc.service &
goimapnotify &
