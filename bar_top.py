from libqtile.bar import Bar
from libqtile.widget import (
    GroupBox,
    Systray,
    Clock,
    TextBox,
    Spacer,
    Mpd2,
    Pomodoro,
    Wttr,
    # Image,
)

from modules.xtheme import colors  # dynamic colors from xres

# Scuffed bar
bar = Bar(
    [
        # Image(
        #     filename="~/Downloads/kitty.png",
        # ),
        TextBox(
            "",
            width=40,
            foreground=colors["bg"],
            background=colors["blue"],
            font="JetBrains Mono Nerd Font",
            fontsize=20,
        ),
        GroupBox(
            fontsize=17,
            disable_drag=True,
            hide_unused=False,
            active=colors["fg1"],
            inactive=colors["gray"],
            highlight_method="line",
            block_highlight_text_color=colors["yellow"],
            borderwidth=0,
            highlight_color=colors["bg"],
            background=colors["bg"],
            font="JetBrains Mono Nerd Font",
            padding=10,
        ),
        Spacer(),
        TextBox(
            " ",
            font="JetBrains Mono Nerd Font",
            background=colors["dark-blue"],
            foreground=colors["bg"],
        ),
        Mpd2(
            width=250,
            font="Source Han Sans JP Bold",
            # fontsize=13,
            # padding=[0, 0, 10, 10],
            background=colors["blue"],
            foreground=colors["bg"],
            # color_progress=[colors["fg"]],
            status_format="{artist} - {title} [{album}]",
            play_states={"pause": "", "play": "", "stop": ""},
            prepare_status={
                "consume": "c",
                "random": "z",
                "repeat": "r",
                "single": "1",
                "updating_db": "U",
            },
            scroll=True,
            idle_format="{play_status} {idle_message}",
            idle_message=" Queue Empty",
        ),
        # Mpris2(),
        # Visualiser(
        #    width=200,
        #    framerate=144,
        #    bar_colour=colors["bg"],
        #    background=colors["dark-blue"],
        #    bars=12,
        # ),  # Lag? instability even
        Spacer(),
        Pomodoro(
            # Widget style
            background=colors["dark-gray"],
            foreground=colors["fg"],
            # Icons
            prefix_active="󱫠 ",
            prefix_inactive="󱎫",
            prefix_break="󱫞 ",
            prefix_long_break="󱫪 ",
            # Text/Icon colors
            color_active=colors["green"],
            color_break=colors["yellow"],
            color_inactive=colors["fg"],
            # Font
            font="JetBrains Mono Nerd Font",
            fontsize=16,
            padding=10,
        ),
        # TextBox(
        #    # Just a separator
        #    "",
        #    background=colors["dark-gray"],
        #    font="JetBrains Mono Nerd Font Bold",
        #    fontsize=16,
        #    padding=10,
        # ),
        Systray(
            # System tray for apps like discord, obs and such
            background=colors["dark-gray"],
            padding=10,
            icon_size=16,
        ),
        # Separator to fix alignment of nerdfont icons
        TextBox(" ", background=colors["dark-gray"], padding=2),
        Wttr(
            location={"Wrocław": "Home"},
            format="%t %c",
            update_interval=30,
            background=colors["blue"],
            foreground=colors["bg"],
            font="JetBrains Mono Nerd Font Bold",
        ),
        TextBox(
            "",
            background=colors["dark-yellow"],
            foreground=colors["bg"],
            padding=10,
            font="JetBrains Mono Nerd Font Bold",
            fontsize=16,
        ),
        TextBox(
            " ",
            background=colors["dark-yellow"],
            foreground=colors["bg"],
            padding=0,
            fontsize=16,
        ),
        Clock(
            background=colors["yellow"],
            foreground=colors["bg"],
            format="%A | %H:%M:%S",
            font="JetBrains Mono Nerd Font Bold",
        ),
    ],
    margin=[5, 5, 5, 5],
    background=colors["bg"],
    foreground=colors["fg"],
    font="JetBrains Mono Nerd Font",
    opacity=1,
    size=25,
)
