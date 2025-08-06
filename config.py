import os
import subprocess

from libqtile import hook

# import layout objects
from libqtile.layout.columns import Columns

# from libqtile.layout.xmonad import MonadThreeCol
from libqtile.layout.stack import Stack
from libqtile.layout.floating import Floating
from libqtile.layout.tile import Tile

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

# from bar_top import bar
#from simpleBar import bar as topbar

# from ui.bars.i3bar import bar
from ui.bars.thinBar import bar

from colorschemes.gruvbox_dark import colors

# from colorschemes.colors import colors

# from colorschemes.nostalgia_dark import colors

# from modules.xtheme import colors


# set mod key "windows/meta" key
mod = "mod4"
# set default terminal
terminal = "kitty"

keys = [
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # rofi shortcuts
    Key([mod], "d", lazy.spawn("rofi -show drun")),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod], "e", lazy.spawn('emacsclient --eval "(emacs-everywhere)"')),
    Key([mod, "control"], "w", lazy.spawn("random-wallpaper")),
    Key(["mod1"], "Tab", lazy.spawn("rofi -show window")),
    Key(["mod1", "shift"], "l", lazy.spawn("betterlockscreen -l")),
    # screenshot shortcuts
    Key(["control"], "Print", lazy.spawn("cropshot")),
    Key([], "Print", lazy.spawn("fullshot")),
    # Key(["control"], "c", lazy.spawn("xclip -selelction clipboard")),
    # media keys
    Key(
        [],
        "XF86AudioRaiseVolume",
        #lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +2000"),
        lazy.spawn("pulsemixer --change-volume +10"),
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pulsemixer --change-volume -10"),
        #lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -2000"),
    ),
    # Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute")),
    Key([], "XF86AudioMicMute", lazy.spawn("sh -c 'pulsemixer --list-sources | cut -f3 | grep Default | awk \"{print \\$2}\" | cut -c 8- | cut -c -2  | xargs -I{} pulsemixer --toggle-mute --id {}'")),
    # brightness keys
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),
    # Key([], "XF86TouchpadToggle", lazy.spawn("xinput disable 11 && xinput disable 10")),
    # mpd shortcuts
    Key(["mod1"], "n", lazy.spawn("mpc next"), desc="play next track"),
    Key(["mod1"], "b", lazy.spawn("mpc previous"), desc="play previous track"),
    Key(["mod1"], "m", lazy.spawn("mpc toggle"), desc="Toggle between play and pause"),
    # Key(["mod1"], "j", lazy.spawn('notify-send "Now playing" subprocess.run(mpc current)')),
    # Toggle floating and fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen mode"),
    Key(
        [mod, "shift"],
        "space",
        lazy.window.toggle_floating(),
        desc="Toggle fullscreen mode",
    ),
    # Keybindings for resizing windows in MonadTall layout
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "control"], "space", lazy.layout.flip()),
    # arrows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    # vim
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key(
        [mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key(
        [mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.grow_left(),
        desc="Grow window to the left",
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Shift to the group above
    Key([mod, "shift"], "j", lazy.screen.prev_group(), desc="Move to the group above"),
    # Shift to the group below
    Key([mod, "shift"], "k", lazy.screen.next_group(), desc="Move to the group below"),
    Key([mod, "shift"], "b", lazy.hide_show_bar("top")),
]

groups = [
    Group(
        "1",
        label="●",
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
        label="●",
        matches=[Match(wm_class="discord"), Match(wm_class="vesktop")],
        layout="stack",
    ),
    Group(
        "3",
        label="●",
        matches=[Match(wm_class="emacs")],
        layout="tile",
    ),
    Group(
        "4",
        label="●",
        matches=[Match(wm_class="Zathura")],
        layout="tile",
    ),
    Group(
        "5",
        label="●",
        matches=[Match(wm_class="steam")],
        layout="stack",
    ),
    Group(
        "6",
        label="●",
        matches=[Match(wm_class="obs")],
        layout="columns",
    ),
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
                "quickbrowser",
                "qutebrowser",
                width=0.5,
                height=0.985,
                y=0.005,
                x=0.26,
                opacity=0.99,
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
                "bitwarden",
                width=0.6,
                height=0.6,
                x=0.2,
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
                opacity=1.0,
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
                "kitty -T cal --hold -e cal -m",
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
                # on_focus_lost_hide=False,
                opacity=1.0,
            ),
            DropDown(
                "emacs",
                "kitty -e emacsclient -nw -c -r",
                # I'm using no gui due to spawning additional window
                # I need to create a proper hook for that TODO
                width=0.5,
                height=0.985,
                y=0.005,
                x=0.26,
                opacity=0.99,
            ),
        ],
    )
)

# extend keys list with keybinding for scratchpad
keys.extend(
    [
        Key(["mod1"], "1", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key(
            ["mod1", "shift"],
            "2",
            lazy.group["scratchpad"].dropdown_toggle("bitwarden"),
        ),
        Key(["mod1"], "2", lazy.group["scratchpad"].dropdown_toggle("music")),
        Key(["mod1"], "3", lazy.group["scratchpad"].dropdown_toggle("mixer")),
        Key(["mod1", "shift"], "3", lazy.group["scratchpad"].dropdown_toggle("OBS")),
        Key(["mod1"], "4", lazy.group["scratchpad"].dropdown_toggle("ranger")),
        Key(["mod1"], "r", lazy.group["scratchpad"].dropdown_toggle("rss")),
        Key(["mod1"], "e", lazy.group["scratchpad"].dropdown_toggle("emacs")),
        Key(["mod1"], "w", lazy.group["scratchpad"].dropdown_toggle("quickbrowser")),
        Key(
            ["mod1", "shift"],
            "4",
            lazy.group["scratchpad"].dropdown_toggle("agenda"),
        ),
        Key(["mod1"], "9", lazy.group["scratchpad"].dropdown_toggle("bitwarden")),
    ]
)

layouts = [
    Stack(
        border_normal=colors["bg1"],
        border_focus=colors["bg2"],
        border_width=2,
        num_stacks=1,
        margin=5,
    ),
    Columns(
        border_normal=colors["dark-cyan"],
        border_focus=colors["cyan"],
        border_width=2,
        border_normal_stack=colors["dark-blue"],
        border_focus_stack=colors["blue"],
        border_on_single=5,
        margin=2,
        margin_on_single=5,
        new_client_position="bottom",
    ),
    Tile(
        master_match=(Match(wm_class="emacs"), Match(wm_class="zathura")),
        border_normal=colors["dark-red"],
        border_focus=colors["red"],
        border_width=2,
        margin=[0, 5, 0, 5],
        margin_on_single=True,
    ),
]

floating_layout = Floating(
    border_normal=colors["bg1"],
    border_focus=colors["bg2"],
    border_width=2,
    float_rules=[
        *Floating.default_float_rules,
        Match(title="OpenRGB"),
        Match(wm_class="bitwarden"),
        # Match(wm_class="nemo"),
        # Match(wm_class="thunar"),
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
