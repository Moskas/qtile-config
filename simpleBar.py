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
)

from colorschemes.gruvbox_dark import colors

# from modules.exchange import ExchangePriceWidget
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


def notify_date():
    date = subprocess.check_output(["date", "+%D"]).decode().strip()
    subprocess.Popen(["notify-send", f"Today is: {date}"])


def exchange(currency):
    value = subprocess.run(
        ["rates", "1", currency, "to", "pln", "--short"], capture_output=True, text=True
    )
    return value.stdout.strip()


separator = "//"
bar = Bar(
    [
        TextBox(
            "",
            width=30,
            foreground=colors["fg"],
            font="JetBrains Mono Nerd Font",
            fontsize=18,
            mouse_callbacks={
                "Button1": lazy.spawn("rofi -show drun"),
                "Button3": lazy.spawn("kitty"),
            },
        ),
        TextBox(separator, font="JetBrainsMono Nerd Font", fontsize=16),
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
            font="JetBrains Mono Nerd Font",
            padding=10,
        ),
        # ExchangePriceWidget(),
        Spacer(),
        Mpd2(
            width=500,
            font="JetBrains Mono Nerd Font",
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
        # TextBox(separator, font="JetBrainsMono Nerd Font", fontsize=16),
        TextBox(
            "XMR %szł" % exchange("xmr"),
            font="JetBrains Mono Nerd Font",
        ),
        TextBox(
            "BTC %szł" % exchange("btc"),
            font="JetBrains Mono Nerd Font",
        ),
        TextBox(separator, font="JetBrainsMono Nerd Font", fontsize=16),
        Wttr(
            location={"Wrocław": "Home"},
            format="%C %f",
            update_interval=30,
            foreground=colors["fg"],
            font="JetBrains Mono Nerd Font",
        ),
        TextBox(
            separator,
            font="JetBrainsMono Nerd Font",
            fontsize=16,
        ),
        Clock(
            foreground=colors["fg"],
            format="%H:%M:%S",
            font="JetBrains Mono Nerd Font",
            mouse_callbacks={
                "Button1": lazy.group["scratchpad"].dropdown_toggle("cal"),
                "Button3": lambda: notify_date(),
            },
        ),
        TextBox(
            separator,
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
