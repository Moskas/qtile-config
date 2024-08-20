from libqtile.lazy import lazy
from libqtile.bar import Bar
from libqtile.widget import (
    CurrentLayout,
    GroupBox,
    Systray,
    Clock,
    TextBox,
    Spacer,
    Mpd2,
    Wttr,
    Prompt,
)

from colorschemes.gruvbox_dark import colors

from modules.distrologo import get_distro_logo

# An attempt to mimick the bar from:
# https://github.com/qxb3/gruvbox.hypr/tree/vim_styled
# Without using any additional plugins and qtile-extras

separator = "|"
font = "JetBrains Mono Nerd Font"

bar = Bar(
    [
        CurrentLayout(
            font=font,
            background=colors["green"],
            foreground=colors["bg"],
        ),
        Prompt(font=font, font_size=16, background=colors["bg2"]),
        GroupBox(
            fontsize=16,
            disable_drag=True,
            hide_unused=True,
            active=colors["gray"],
            inactive=colors["bg2"],
            highlight_method="line",
            block_highlight_text_color=colors["fg"],
            borderwidth=0,
            highlight_color=colors["bg"],
            background=colors["bg"],
            font=font,
            padding=10,
        ),
        Spacer(),
        Mpd2(
            width=300,
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
        # TextBox(
        #    f"{get_distro_logo()}",
        #    width=35,
        #    foreground=colors["fg"],
        #    background=colors["bg2"],
        #    font=font,
        #    fontsize=18,
        #    mouse_callbacks={
        #        "Button1": lazy.spawn("rofi -show drun"),
        #        "Button3": lazy.spawn("kitty"),
        #    },
        # ),
        Wttr(
            location={"Wrocław": "Home"},
            format="%C %f",
            update_interval=30,
            foreground=colors["fg"],
            background=colors["bg1"],
            font=font,
        ),
        Systray(
            background=colors["bg1"],
        ),
        Clock(
            foreground=colors["fg"],
            background=colors["bg2"],
            format="%H:%M:%S",
            font=font,
            mouse_callbacks={
                "Button1": lazy.group["scratchpad"].dropdown_toggle("cal"),
                # "Button3": lambda: notify_date(),
            },
        ),
    ],
    font=font,
    font_size=16,
    opacity=1,
    size=25,
    background=colors["bg"],
    foreground=colors["fg"],
)
