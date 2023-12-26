import os
import subprocess
from libqtile.lazy import lazy
from libqtile.bar import Bar
from libqtile.widget import (
    GroupBox,
    Systray,
    Clock,
    TextBox,
    Spacer,
    Mpd2,
    Wttr,
)
from modules.distrologo import get_distro_logo
from modules.battery import has_battery

# Conditional import because on my desktop I'm using gruvbox colorscheme and on my laptop I'm using solarized
if os.uname().nodename == "roon":
    from colorschemes.solarized_dark import colors
else:
    from colorschemes.gruvbox_dark import colors


def notify_date():
    date = subprocess.check_output(["date", "+%D"]).decode().strip()
    subprocess.Popen(["notify-send", f"Today is: {date}"])


# Variables for styling modules
font = "JetBrainsMono Nerd Font"
separator = TextBox("|", font=font, fontsize=16, foreground=colors["fg"])


if has_battery() is True:
    from libqtile.widget import Battery

    battery_widget = Battery(
        format="{char} {percent:2.0%}",
        fontsize=16,
        font=font,
        foreground=colors["fg"],
        discharge_foreground=colors["fg"],
        low_percentage=0.2,
        notify_bellow=30,
        full_char="󰁹",
        char="󰁹",
        charge_char="󱟠",
        discharge_char="󱟞",
        empty_char="󰂎",
        unknown_char="󱠴",
        show_short_text=False,
    )

else:
    battery_widget = TextBox()


bar = Bar(
    [
        TextBox(
            get_distro_logo(),
            width=30,
            foreground=colors["fg"],
            font=font,
            fontsize=18,
            mouse_callbacks={
                "Button1": lazy.spawn("rofi -show drun"),
                "Button3": lazy.spawn("kitty"),
            },
        ),
        separator,
        GroupBox(
            fontsize=16,
            disable_drag=True,
            hide_unused=False,
            active=colors["fg1"],
            inactive=colors["inactive"],
            highlight_method="line",
            block_highlight_text_color=colors["cyan"],
            borderwidth=0,
            highlight_color=colors["bg"],
            background=colors["bg"],
            font=font,
            padding=10,
        ),
        Spacer(),
        Mpd2(
            width=500,
            font=font,
            fontsize=16,
            foreground=colors["fg"],
            status_format="{artist} - {title} [{album}]",
            scroll=True,
            idle_format="{play_status} {idle_message}",
            idle_message="Queue Empty",
            mouse_callbacks={
                "Button2": lazy.group["scratchpad"].dropdown_toggle("music"),
            },
        ),
        Spacer(),
        separator,
        Wttr(
            location={"Wrocław": "Home"},
            format="%C %f",
            update_interval=30,
            foreground=colors["fg"],
            font=font,
            fontsize=16,
        ),
        separator,
        Clock(
            foreground=colors["fg"],
            format="%H:%M:%S",
            font=font,
            fontsize=16,
            mouse_callbacks={
                "Button1": lazy.group["scratchpad"].dropdown_toggle("cal"),
                "Button3": lambda: notify_date(),
            },
        ),
        separator,
        battery_widget,
        Systray(
            # System tray for apps like discord, obs and such
            background=colors["bg"],
            padding=10,
            icon_size=16,
        ),
        TextBox(
            " ",
            font=font,
            fontsize=16,
            width=10,
        ),
    ],
    # margin=[5, 5, 5, 5],
    background=colors["bg"],
    foreground=colors["fg"],
    font=font,
    opacity=1,
    size=25,
)
