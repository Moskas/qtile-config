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


def notify_current_song():
    # Run the "mpc current" command and capture its output
    mpc_output = subprocess.check_output(["mpc", "current"]).decode().strip()

    # Split artist - title
    artist, song_title = mpc_output.split(" - ")

    # Construct the message string to pass to "notify-send"
    message = f"{artist}\n{song_title}"

    # Call "notify-send" with the message string
    subprocess.Popen(["notify-send", "Now playing:", message])


# Scuffed bar
bar = Bar(
    [
        # TextBox(
        #    "",
        #    width=40,
        #    foreground=colors["inactive"],
        #    background=colors["blue"],
        #    font="JetBrains Mono Nerd Font",
        #    fontsize=20,
        # ),
        GroupBox(
            fontsize=17,
            disable_drag=True,
            hide_unused=False,
            active=colors["gray"],
            inactive=colors["bg2"],
            highlight_method="line",
            block_highlight_text_color=colors["fg"],
            borderwidth=0,
            highlight_color=colors["bg"],
            background=colors["bg"],
            font="JetBrains Mono Nerd Font",
            padding=10,
        ),
        Spacer(),
        # TextBox(
        #    "",
        #    font="JetBrains Mono Nerd Font",
        #    background=colors["dark-blue"],
        #    foreground=colors["bg"],
        #    width=27,
        #    mouse_callbacks={"Button1": lambda: notify_current_song()},
        # ),
        Mpd2(
            width=300,
            font="JetBrains Mono Nerd Font Bold",
            # fontsize=13,
            # padding=[0, 0, 10, 10],
            foreground=colors["fg"],
            # color_progress=[colors["fg"]],
            status_format="{artist} - {title} [{album}]",
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
        # Pomodoro(
        #    # Widget style
        #    background=colors["bg"],
        #    foreground=colors["fg"],
        #    # Icons
        #    prefix_active="󱫠 ",
        #    prefix_inactive="󱎫",
        #    prefix_break="󱫞 ",
        #    prefix_long_break="󱫪 ",
        #    # Text/Icon colors
        #    color_active=colors["green"],
        #    color_break=colors["yellow"],
        #    color_inactive=colors["fg"],
        #    # Font
        #    font="JetBrains Mono Nerd Font",
        #    fontsize=16,
        #    padding=10,
        # ),
        # TextBox(
        #    # Just a separator
        #    "",
        #    background=colors["gray"],
        #    font="JetBrains Mono Nerd Font Bold",
        #    fontsize=16,
        #    padding=10,
        # ),
        # Separator to fix alignment of nerdfont icons
        TextBox("|", font="JetBrainsMono Nerd Font", fontsize=16),
        Wttr(
            location={"Wrocław": "Home"},
            format="%C %t",
            update_interval=30,
            foreground=colors["fg"],
            font="JetBrains Mono Nerd Font Bold",
        ),
        #  TextBox(
        #    "",
        #    background=colors["dark-yellow"],
        #    foreground=colors["bg"],
        #    padding=10,
        #    font="JetBrains Mono Nerd Font Bold",
        #    fontsize=16,
        #    mouse_callbacks={
        #            'Button1': lazy.spawn("kitty -T cal --hold -e cal "),
        #            'Button3': lazy.spawn("notify-send Close Calendar"),
        #    },
        #  ),
        #  TextBox(
        #    " ",
        #    background=colors["dark-yellow"],
        #    foreground=colors["bg"],
        #    padding=0,
        #    fontsize=16,
        #  ),
        TextBox(
            "|",
            font="JetBrainsMono Nerd Font",
            fontsize=16,
        ),
        Clock(
            foreground=colors["fg"],
            format="%A %H:%M:%S",
            font="JetBrains Mono Nerd Font Bold",
            mouse_callbacks={
                "Button1": lazy.group["scratchpad"].dropdown_toggle("cal"),
                "Button3": lazy.spawn("notify-send Close Calendar"),
            },
        ),
        TextBox(
            "|",
            font="JetBrainsMono Nerd Font",
            fontsize=16,
        ),
        Systray(
            # System tray for apps like discord, obs and such
            background=colors["bg"],
            padding=10,
            icon_size=16,
        ),
        TextBox(
            " ",
            font="JetBrainsMono Nerd Font",
            fontsize=16,
            width=10,
        ),
    ],
    # margin=[5, 5, 5, 5],
    background=colors["bg"],
    foreground=colors["fg"],
    font="JetBrains Mono Nerd Font",
    opacity=1,
    size=25,
)
