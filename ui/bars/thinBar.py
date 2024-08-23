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
    ImapWidget,
    Pomodoro,
    GenPollText,
    DoNotDisturb,
)

# from colorschemes.colors import colors
from colorschemes.gruvbox_dark import colors

import subprocess
from modules.distrologo import get_distro_logo

separator = "|"
font = "JetBrains Mono Nerd Font"

widget_defaults = dict(
    font=font,
    fontsize=16,
    background=colors["bg"],
    foreground=colors["fg"],
)

bar = Bar(
    [
        TextBox(
            get_distro_logo(),
            width=30,
            foreground=colors["blue"],
            font="Iosevka Nerd Font",
            fontsize=16,
            mouse_callbacks={
                "Button1": lazy.spawn("rofi -show drun"),
                "Button3": lazy.spawn("kitty"),
            },
        ),
        GroupBox(
            fontsize=16,
            disable_drag=True,
            hide_unused=False,
            active=colors["gray"],
            inactive=colors["bg2"],
            highlight_method="line",
            block_highlight_text_color=colors["fg"],
            borderwidth=0,
            highlight_color=colors["bg"],
            background=colors["bg"],
            font=font,
            # padding=10,
        ),
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
            fontsize=12,
        ),
        Spacer(),
        Systray(
            # System tray for apps like discord, obs and such
            background=colors["bg"],
            padding=5,
            icon_size=18,
        ),
        # TextBox(
        #    " ",
        #    font=font,
        #    fontsize=16,
        #    width=10,
        #    foreground=colors["fg"],
        # ),
        Wttr(
            location={"Wrocław": "Home"},
            format="%C %f",
            update_interval=30,
            foreground=colors["fg"],
            font=font,
            fontsize=12,
        ),
        Clock(
            foreground=colors["fg"],
            format="%H:%M:%S",
            font=font,
            mouse_callbacks={
                "Button1": lazy.group["scratchpad"].dropdown_toggle("cal"),
                # "Button3": lambda: notify_date(),
            },
            fontsize=12,
        ),
        DoNotDisturb(
            enabled_icon="󱏧 ",
            disabled_icon="󰂚 ",
            fontsize=16,
        ),
    ],
    margin=[5, 5, 5, 5],
    background=colors["bg"],
    foreground=colors["fg"],
    font=font,
    opacity=1,
    size=24,
)
