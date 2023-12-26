from libqtile.lazy import lazy
from libqtile.config import Key

# set mod key "windows/meta" key
mod = "mod4"
terminal = "kitty"


binds = [
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # rofi shortcuts
    Key([mod], "d", lazy.spawn("rofi -show drun")),
    Key(["mod1"], "Tab", lazy.spawn("rofi -show window")),
    Key(["mod1", "shift"], "l", lazy.spawn("betterlockscreen -l")),
    # screenshot shortcuts
    Key(["control"], "Print", lazy.spawn("flameshot gui -c")),
    Key([], "Print", lazy.spawn("flameshot screen -c")),
    # Key(["control"], "c", lazy.spawn("xclip -selelction clipboard")),
    # media keys
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +2000"),
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -2000"),
    ),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    # brightness keys
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),
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
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

# for i in groups:
#    binds.extend(
#        [
#            # mod1 + letter of group = switch to group
#            Key(
#                [mod],
#                i.name,
#                lazy.group[i.name].toscreen(),
#                desc="Switch to group {}".format(i.name),
#            ),
#            # Or, use below if you prefer not to switch to that group.
#            # mod1 + shift + letter of group = move focused window to group
#            Key(
#                [mod, "shift"],
#                i.name,
#                lazy.window.togroup(i.name),
#                desc="move focused window to group {}".format(i.name),
#            ),
#        ]
#    )

# Add binds for scratchpad
binds.extend(
    [
        Key(["mod1"], "1", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key(["mod1"], "2", lazy.group["scratchpad"].dropdown_toggle("music")),
        Key(["mod1"], "3", lazy.group["scratchpad"].dropdown_toggle("mixer")),
        Key(["mod1", "shift"], "3", lazy.group["scratchpad"].dropdown_toggle("OBS")),
        Key(["mod1"], "4", lazy.group["scratchpad"].dropdown_toggle("ranger")),
        Key(["mod1"], "5", lazy.group["scratchpad"].dropdown_toggle("rss")),
        Key(
            ["mod1", "shift"],
            "4",
            lazy.group["scratchpad"].dropdown_toggle("agenda"),
        ),
        Key(["mod1"], "9", lazy.group["scratchpad"].dropdown_toggle("bitwarden")),
    ]
)
