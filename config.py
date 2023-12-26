import os
import subprocess

from libqtile import hook

# import layout objects
from libqtile.layout.columns import Columns
from libqtile.layout.xmonad import MonadThreeCol
from libqtile.layout.stack import Stack
from libqtile.layout.floating import Floating

# import widgets and bars
from libqtile.config import (
    Click,
    Drag,
    DropDown,
    Group,
    Key,
    Match,
    ScratchPad,
    Screen,
)

from libqtile.lazy import lazy

# Import keybinds
from binds.binds import binds

# Import qtile bar
from bars.simpleBar import bar

if os.uname().nodename == "roon":
    from colorschemes.solarized_dark import colors
else:
    from colorschemes.gruvbox_dark import colors

# set mod key "windows/meta" key
mod = "mod4"
# set default terminal
terminal = "kitty"

keys = binds

groups = [
    Group(
        "1",
        label="󰖟",
        matches=[
            Match(wm_class="firefox"),
            Match(wm_class="brave-browser"),
            Match(wm_class="qutebrowser"),
            Match(wm_class="nyxt"),
        ],
        layout="stack",
    ),
    Group(
        "2",
        label="󰙯",
        matches=[Match(wm_class="discord"), Match(wm_class="signal")],
        layout="stack",
    ),
    Group(
        "3",
        label="",
        matches=[Match(wm_class="emacs")],
        layout="columns",
    ),
    Group("4", label="󰠮", matches=[Match(wm_class="Zathura")], layout="monadthreecol"),
    Group("5", label="", matches=[Match(wm_class="steam")], layout="columns"),
    Group(
        "6",
        label="󰄀",
        matches=[Match(wm_class="obs")],
        layout="columns",
    ),
    # Group("7", label="", layout="zoomy"),
    # Group("8", label="󰇮", matches=[Match(wm_class="Geary")], layout="columns"),
    # Group("9", label="", layout="columns"),
    # Group(
    #    "0",
    #    label="󰎆",
    #    matches=[Match(wm_class="Spotify"), Match(wm_class="mpdevil")],
    #    layout="stack",
    # ),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # mod1 + shift + letter of group = move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name),
            ),
        ]
    )

# Append scratchpad with dropdowns to groups
groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term",
                "kitty",
                width=0.6,
                height=0.7,
                x=0.2,
                y=0.005,
                opacity=0.9,
            ),
            DropDown(
                "agenda",
                "kitty -e emacsclient -c -nw -e (org-agenda)",
                width=0.6,
                height=0.7,
                x=0.2,
                y=0.0,
                opacity=0.9,
            ),
            DropDown(
                "pixel",
                "kitty -e scrcpy -b 30M -w -S --max-fps=90",
                width=0.6,
                height=0.7,
                x=0.2,
                y=0.005,
                opacity=0.9,
            ),
            DropDown(
                "stock",
                "kitty -e tickrs",
                width=0.6,
                height=0.7,
                x=0.2,
                y=0.005,
                opacity=0.9,
            ),
            DropDown(
                "mixer",
                "kitty -e pulsemixer",
                width=0.4,
                height=0.2,
                x=0.3,
                y=0.005,
                opacity=0.9,
            ),
            DropDown(
                "webplayer",
                "qutebrowser",
                width=0.8,
                height=0.8,
                x=0.1,
                y=0.005,
                opacity=1.0,
            ),
            DropDown(
                "music",
                "kitty -e ncmpcpp",
                width=0.6,
                height=0.7,
                x=0.2,
                y=0.005,
                opacity=0.9,
            ),
            DropDown(
                "bitwarden",
                "bitwarden-desktop",
                width=0.4,
                height=0.6,
                x=0.3,
                y=0.1,
                opacity=1,
            ),
            DropDown(
                "ranger",
                "kitty -e ranger /home/moskas/",
                width=0.6,
                height=0.7,
                x=0.2,
                y=0.1,
                opacity=0.9,
            ),
            DropDown(
                "OBS",
                "obs",
                width=0.6,
                height=0.7,
                x=0.2,
                y=0.1,
                opacity=0.9,
            ),
            DropDown(
                "cal",
                "kitty -T cal --hold -e cal",
                width=0.2,
                height=0.25,
                x=0.795,
                y=0.005,
                opacity=0.9,
            ),
            DropDown(
                "rss",
                "kitty -e newsboat",
                width=0.5,
                height=0.985,
                y=0.005,
                x=0.26,
            ),
        ],
    )
)

layouts = [
    Stack(
        border_normal=colors["fg2"],
        border_focus=colors["cyan"],
        border_width=3,
        num_stacks=1,
        margin=5,
    ),
    # MonadTall(
    #    border_normal=colors["fg2"],
    #    border_focus=colors["red"],
    #    margin=5,
    #    border_width=4,
    #    single_border_width=4,
    #    single_margin=5,
    # ),
    Columns(
        border_normal=colors["fg2"],
        border_focus=colors["blue"],
        border_width=3,
        border_normal_stack=colors["fg2"],
        border_focus_stack=colors["magenta"],
        border_on_single=3,
        margin=5,
        margin_on_single=5,
        new_client_position="bottom",
    ),
    MonadThreeCol(
        border_normal=colors["fg2"],
        border_focus=colors["yellow"],
        margin=5,
        border_width=3,
        single_border_width=3,
        single_margin=5,
        new_client_position="bottom",
    ),
]

floating_layout = Floating(
    border_normal=colors["fg2"],
    border_focus=colors["blue"],
    border_width=3,
    float_rules=[
        *Floating.default_float_rules,
        Match(title="OpenRGB"),
        Match(title="Pixel 6"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="stacer"),
        Match(wm_class="bitwarden"),
        Match(wm_class="nemo"),
        Match(wm_class="thunar"),
        Match(title="notificationtoasts_8_desktop"),
        Match(wm_class="ranger,ranger"),
    ],
)

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
widget_defaults = dict(
    fontsize=13,
    foreground=colors["fg"],
)

extension_defaults = widget_defaults.copy()

screens = [Screen(top=bar)]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = ""
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "kittywm"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])


@hook.subscribe.client_new
def disable_floating(window):
    rules = [Match(wm_class="mpv")]

    if any(window.match(rule) for rule in rules):
        window.togroup(qtile.current_group.name)
        window.cmd_disable_floating()
