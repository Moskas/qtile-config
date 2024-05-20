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
)

from colorschemes.gruvbox_dark import colors

# from colorschemes.nostalgia_dark import colors


import subprocess
from modules.distrologo import get_distro_logo

# from modules.battery import has_battery


# def notify_current_song():
#     mpc_output = subprocess.check_output(["mpc", "current"]).decode().strip()
#     artist, song_title = mpc_output.split(" - ")
#     message = f"{artist}\n{song_title}"
#     subprocess.Popen(["notify-send", "Now playing:", message])


# def notify_date():
#     date = subprocess.check_output(["date", "+%D"]).decode().strip()
#     subprocess.Popen(["notify-send", f"Today is: {date}"])


# def exchange(currency):
#    value = (
#        subprocess.check_output(["rates", "1", currency, "to", "pln", "--short"])
#        .decode()
#        .strip()
#    )
#    return value
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
            foreground=colors["fg"],
            font="Iosevka Nerd Font",
            fontsize=18,
            mouse_callbacks={
                "Button1": lazy.spawn("rofi -show drun"),
                "Button3": lazy.spawn("kitty"),
            },
        ),
        TextBox(separator, font=font, fontsize=16, foreground=colors["fg"]),
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
        # TextBox(separator, font=font, fontsize=16),
        # TextBox(
        #    "XMR %szł" % exchange("xmr"),
        #    font=font,
        # ),
        # TextBox(
        #    "BTC %szł" % exchange("btc"),
        #    font=font,
        # ),
        #        TextBox(separator, font=font, fontsize=16, foreground=colors["fg"]),
        #        GenPollText(
        #            foreground=colors["fg"],
        #            name="BTC",
        #            fmt="{} BTC",
        #            update_interval=60,
        #            func=lambda: subprocess.check_output(
        #                ["rates", "1", "btc", "to", "pln", "--short"]
        #            )
        #            .strip()
        #            .decode(),
        #        ),
        #        TextBox(separator, font=font, fontsize=16, foreground=colors["fg"]),
        #        GenPollText(
        #            foreground=colors["fg"],
        #            name="XMR",
        #            fmt="{} XMR",
        #            update_interval=60,
        #            func=lambda: subprocess.check_output(
        #                ["rates", "1", "xmr", "to", "pln", "--short"]
        #            )
        #            .strip()
        #            .decode(),
        #        ),
        TextBox(separator, font=font, fontsize=16, foreground=colors["fg"]),
        Wttr(
            location={"Wrocław": "Home"},
            format="%C %f",
            update_interval=30,
            foreground=colors["fg"],
            font=font,
        ),
        TextBox(
            separator,
            font=font,
            fontsize=16,
            foreground=colors["fg"],
        ),
        Clock(
            foreground=colors["fg"],
            format="%H:%M:%S",
            font=font,
            mouse_callbacks={
                "Button1": lazy.group["scratchpad"].dropdown_toggle("cal"),
                # "Button3": lambda: notify_date(),
            },
        ),
        TextBox(
            separator,
            font=font,
            fontsize=16,
            foreground=colors["fg"],
        ),
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
            foreground=colors["fg"],
        ),
    ],
    # margin=[5, 5, 5, 5],
    background=colors["bg"],
    foreground=colors["fg"],
    font=font,
    opacity=1,
    size=25,
)
