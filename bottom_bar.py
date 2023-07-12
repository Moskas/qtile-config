from libqtile.bar import Bar

from colorschemes.gruvbox_dark import colors

from libqtile.widget.spacer import Spacer
from libqtile.widget.open_weather import OpenWeather
from libqtile.widget.check_updates import CheckUpdates


bottom_bar = Bar(
    [
        CheckUpdates(
            colour_have_updates=colors["red"],
            colour_no_updates=colors["fg"],
            display_format=" {updates}",
            distro="Arch",
            execute="kitty -e /usr/bin/paru -Syyu",
            no_update_string="",
            update_interval="60",
        ),
        OpenWeather(
            location="Wrocław,PL",
            language="PL",
            format="{location_city}: {main_temp} °{units_temperature} | {icon} | {sunrise} {sunset} | {wind_speed} m/s {wind_direction}",
        ),
        Spacer(),
        # Wallpaper(
        # directory="~/.config/wallpapers/gruvbox/dark",
        # option="fill",
        # wallpaper_command=[
        #    "feh",
        #    "--bg-fill",
        #    "~/.config/wallpapers/gruvbox/**",
        #    "--randomize",
        # ],
        # random_selection=True,
        # # only works when you have single directory selected
        # I have dark and light variants in gruvbox directory so that's a no go
        # label=" ",
        # ),
    ],
    # margin=[5, 5, 5, 5],
    background=colors["bg"],
    foreground=colors["fg"],
    font="JetBrains Mono Nerd Font",
    opacity=1,
    size=25,
)
