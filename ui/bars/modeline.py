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

from colorschemes.gruvbox_dark import colors


import subprocess
from modules.distrologo import get_distro_logo

# from modules.battery import has_battery

separator = "//"
font = "JetBrains Mono Nerd Font"

bar = Bar(
    [
        GroupBox(
            fontsize=16,
            disable_drag=True,
            hide_unused=False,
            active=colors["gray"],
            inactive=colors["bg2"],
            highlight_method="line",
            block_highlight_text_color=colors["fg"],
            borderwidth=0,
            highlight_color=colors["bg1"],
            background=colors["bg1"],
            font=font,
            padding=10,
        ),
        # ExchangePriceWidget(),
        Spacer(),
        Mpd2(
            width=500,
            font=font,
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
        Wttr(
            location={"Wrocław": "Home"},
            format="%C %f",
            update_interval=30,
            foreground=colors["bg"],
            background=colors["dark-blue"],
            font=font,
        ),
        Clock(
            format="%H:%M:%S",
            font=font,
            mouse_callbacks={
                "Button1": lazy.group["scratchpad"].dropdown_toggle("cal"),
                # "Button3": lambda: notify_date(),
            },
            background=colors["blue"],
            foreground=colors["bg"],
        ),
        Systray(
            # System tray for apps like discord, obs and such
            background=colors["bg2"],
            padding=10,
            icon_size=16,
        ),
        TextBox(
            " ",
            font=font,
            fontsize=16,
            width=10,
            background=colors["bg2"],
        ),
    ],
    # margin=[5, 5, 5, 5],
    background=colors["bg"],
    foreground=colors["fg"],
    font=font,
    opacity=1,
    size=25,
)
