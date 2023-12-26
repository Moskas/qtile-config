#!/usr/bin/env bash

xrandr --output DP-0 --mode 1920x1080 --rate 143.98 --dpi 100 &
#/home/moskas/.scripts/random-gruv-wall
#random-wallpaper &
feh --bg-fill --randomize /home/moskas/Pictures/Wallpapers/solarized/dark/*.{png,jpg} &
#openrgb -p Red &
#betterlockscreen -u ~/.config/wallpapers/gruvbox/**/* 
setxkbmap pl &
#dunst &
#picom --experimental-backends & # 
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
# Random apps
discord &
nicotine &

# mpd notification
mpd-notify-rs &
#/home/moskas/.local/share/applications/mpd-notify-rs &
#mpDris2 &

# Rival 3 mouse sensitivity
#rivalcfg -s 800 

# SSHFS for local NAS
#sshfs -o ~/.ssh/optiplex optiplex.home:~ ~/nas
#systemctl restart --user emacs.service # For some reason it has issues on launch
