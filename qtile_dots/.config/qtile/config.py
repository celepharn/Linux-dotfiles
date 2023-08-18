# -*- coding: utf-8 -*-

##
# Author: bw3u <berkcan@vivaldi.net>
# Github: @bw3u
# Gitlab: @bw3u
# Reddit: @panlazy
#
# License: MIT

# Imports #
import os
import subprocess
from libqtile import qtile
from libqtile.config import (
    Group,
    KeyChord,
    Key,
    Match,
    Screen,
    EzClick as Click,
    EzDrag as Drag,
)
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

# Defaults #
mod = "mod4"  # Setting mod key to "SUPER"
term = "alacritty"  # Setting terminal to "kitty"
browser = "firefox"  # Setting browser to "Firefox Developer Edition"

# Keybindings #
keys = [
    Key([mod], "Return", lazy.spawn(term), desc="Launches default terminal"),
    Key([mod, "shift"], "d", lazy.spawn(os.path.expanduser("~/.config/sunset/scripts/launcher.sh")),
        desc="Rofi launcher",
    ),
    #Key([mod], "y", lazy.spawn("rofimoji -a copy"), desc="Launches rofimoji"),
    Key(
        [mod, "control"],
        "q",
        lazy.spawn(os.path.expanduser("~/.config/sunset/scripts/powermenu.sh")),
        desc="Rofi powermenu",
    ),
    #Key(
    #    [mod, "shift", "control"],
    #    "l",
    #    lazy.spawn("betterlockscreen -l"),
    #    desc="Lock screen",
    #),
    #Key(
    #    [mod, "control"],
    #    "space",
    #    lazy.widget["keyboardlayout"].next_keyboard(),
    #    desc="Next kbd layout.",
    #),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"), # Didn't configured the bar properly, looks like shit.
    # Qtile controls
    Key([mod], "Tab", lazy.next_layout(), desc="Switch layout"),
    Key([mod], "q", lazy.window.kill(), desc="Kill active window"),
    #Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill every window"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "shift"], "e", lazy.shutdown(), desc="Quit qtile"),
    # Workspace controls.
    Key([mod], "j", lazy.layout.down(), desc="Move focus down in current stack pane"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus left in current stack pane"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus right in current stack pane"),
    #Key([mod], "Down", lazy.layout.down(), desc="Move focus down in current stack pane"),
    #Key([mod], "Up", lazy.layout.up(), desc="Move focus up in current stack pane"),
    #Key([mod], "Left", lazy.layout.left(), desc="Move focus left in current stack pane"),
    #Key([mod], "Right", lazy.layout.right(), desc="Move focus right in current stack pane"),

    Key(
        [mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        lazy.layout.section_left(),
        desc="Move windows left in current stack",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        lazy.layout.section_right(),
        desc="Move windows right in current stack",
    ),
    #Key([mod], "n", lazy.layout.normalize(), desc="normalize window size ratios"),
    #Key(
    #    [mod],
    #    "m",
    #    lazy.layout.maximize(),
    #    desc="toggle window between minimum and maximum sizes",
    #),
    #Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="toggle floating"),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc="toggle fullscreen"),
    ## Stack controls
    Key(
        [mod, "shift"],
        "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc="Switch which side main pane occupies (XMonadTall)",
    ),
    Key(
        [mod],
        "space",
        lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack",
    ),
    Key(
        [mod, "shift"],
        "space",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Emacs keybindings, CTRL+e -> 'key'.
    KeyChord(
        ["control"],
        "e",
        [
            Key([], "e", lazy.spawn("emacsclient -c -a 'emacs'"), desc="Launch Emacsclient"),
            Key([], "g", lazy.spawn("emacs"), desc="Launch Emacs in GUI mode")
        ],
    ),
    # Application keybindings
    # Key([mod, "shift"], "d", lazy.spawn("pcmanfm"), desc="Launch PCManFM"),
    #Key([mod], "n", lazy.spawn("thunar"), desc="Launch Thunar"),
    Key([mod], "n", lazy.spawn("urxvt -e 'ranger'"), desc="Launch Thunar"),
    Key([mod], "e", lazy.spawn("telegram-desktop"), desc="Launch TelegramDesktop"),
    Key([mod], "r", lazy.spawn("discord"), desc="Launch Discord"),
    Key([mod], "f", lazy.spawn("firefox"), desc="Launch Firefox"),
    Key([mod], "c", lazy.hide_show_bar(), desc="Toggle visibility of Bar"),
    Key([mod], "w", lazy.spawn("qutebrowser"), desc="Launch Qutebrowser"),
    Key([mod], "p", lazy.spawn("chromium"), desc="Launch Chromium"),
    Key([mod], "m", lazy.spawn("steam"), desc="Launch Steam"),
    Key([mod], "s", lazy.spawn("spotify"), desc="Launch Spotify"),
    Key([mod], "u", lazy.spawn("freetube"), desc="Launch FreeTube"),
    #Key([], "Print", lazy.spawn("scrot '%Y-%m-%d-%T.jpg' -e 'mv $f ~/Pictures/Screenshots' && notify-send 'Screenshot' 'file saved in ~/Pictures/Screenshots' --icon=dialog-information"), desc="Screenshot"),
    Key([mod], "a", lazy.spawn("emacs"), desc="Launch emacs"),
    Key([mod], "b", lazy.spawn("thunderbird"), desc="Launch thunderbird"),
    Key([mod], "o", lazy.spawn("dolphin-emu"), desc="Launch dolphin"),
    # Media Keys
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn(os.path.expanduser("~/.config/dunst/volume.sh up"))
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn(os.path.expanduser("~/.config/dunst/volume.sh down"))
    ),
    Key(
        [],
        "XF86AudioMicMute",
        lazy.spawn(os.path.expanduser("~/.config/dunst/volume.sh mute"))
    ),
    Key(
        [], 
        "XF86AudioMute", 
        lazy.spawn(os.path.expanduser("~/.config/dunst/volume.sh mute"))
    ),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    # Mpris usage example.
    # Key(
    #    [],
    #    "XF86AudioPlay",
    #    lazy.spawn(
    #        "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify "
    #        "/org/mpris/MediaPlayer2 "
    #        "org.mpris.MediaPlayer2.Player.PlayPause"
    #    ),
    #    desc="Audio play",
    # ),
    # Key(
    #    [],
    #    "XF86AudioNext",
    #    lazy.spawn(
    #        "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify "
    #        "/org/mpris/MediaPlayer2 "
    #        "org.mpris.MediaPlayer2.Player.Next"
    #    ),
    #    desc="Audio next",
    # ),
    # Key(
    #    [],
    #    "XF86AudioPrev",
    #    lazy.spawn(
    #        "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify "
    #        "/org/mpris/MediaPlayer2 "
    #        "org.mpris.MediaPlayer2.Player.Previous"
    #    ),
    #    desc="Audio previous",
    # ),
]


groups = [
    Group(
        "1", 
        label="", 
        matches=[
            Match(wm_class=["qutebrowser", "firefox"]),
        ],
    ),
    Group(
        "2",
        label="ﲵ",
        matches=[
            Match(wm_class=["Alacritty"]),
        ],
    ),
    Group(
        "3",
        label="",
        matches=[
            Match(wm_class=["Thunar", "URxvt"]),
        ],
    ),
    Group(
        "4",
        label="ﯟ",
        matches=[
            Match(wm_class=["code-oss", "Emacs"]),
        ],
    ),
    Group(
        "5",
         label="",
         matches=[
             Match(wm_class=["Spotify"]),
         ],
    ),
    Group(
        "6",
        label="",
        matches=[
            Match(wm_class=["discord", "TelegramDesktop"])
        ],
    ),
    Group(
        "7",
        label="",
        matches=[
            Match(wm_class=["Lutris", "dolphin-emu", "Steam"])
        ],
    ),
    Group(
        "8",
        label="",
        matches=[
            Match(wm_class=["FreeTube", "Chromium", "mpv"])
        ],
    ),
    Group(
        "9",
        label="",
        matches=[
            Match(wm_class=["steam_app_252950", "steam_app_813780", "steam_app_1190460",
                            "ShadowOfTheTombRaider", "steam_app_356190", "sc2_x64.exe", "hollow_knight.x86_64",
                            "Thunderbird", "steam_app_976730", "steam_app_448510", "steam_app_1604030"])
        ],
    ),
    Group(
        "0", 
        label="",
        matches=[
            Match(wm_class=["battle.net.exe", "explorer.exe", "qBittorrent"]),
        ],
),
]

for i in range(len(groups)):
    keys.append(Key([mod], str((i)), lazy.group[str(i)].toscreen()))
    keys.append(
        Key([mod, "shift"], str((i)), lazy.window.togroup(str(i), switch_group=True))
    )

# blue color scheme. (["main color", "2nd color, if diff will be gradient"])
colors = [
    ["#1e2021", "#1e2021"],  # 0 Dark
    ["#ffffff", "#ffffff"],  # 1 White
    ["#999999", "#999999"],  # 2 Gray
    ["#c6dbf0", "#c6dbf0"],  # 3 blue4
    ["#aed1e6", "#aed1e6"],  # 4 blue3
    ["#a0c4e2", "#a0c4e2"],  # 5 blue2
    ["#85c7de", "#85c7de"],  # 6 blue1 the higher the number the lightest the color is
    ["#ffa69e", "#ffa69e"],  # 7 red
]

#pastel color scheme
#colors = [
#    ["#1e2021", "#1e2021"],  # 0 dark
#    ["#ffffff", "#ffffff"],  # 1 white
#    ["#999999", "#999999"],  # 2 gray
#    ["#fcf6bd", "#fcf6bd"],  # 3 yellow
#    ["#d0f4de", "#d0f4de"],  # 4 green
#    ["#e4c1f9", "#e4c1f9"],  # 5 pink
#    ["#a9def9", "#a9def9"],  # 6 blue
#]

#pastel2 color scheme
#colors = [
#    ["#1e2021", "#1e2021"],  # 0 dark
#    ["#ffffff", "#ffffff"],  # 1 white
#    ["#999999", "#999999"],  # 2 gray
#    ["#ffa69e", "#ffa69e"],  # 3 yellow
#    ["#faf3dd", "#faf3dd"],  # 4 green
#    ["#b8f2e6", "#b8f2e6"],  # 5 pink
#    ["#a9def9", "#a9def9"],  # 6 blue
#]

layout_theme = {
    "border_width": 1,
    "margin": 6,
    "border_focus": "#a0c4e2",
    "border_normal": "#1e2021",
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.Floating(**layout_theme),
]


# Widgets #

widget_defaults = dict(
    font="Noto Sans Font",
    fontsize=10,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.Sep(
                #    padding=6,
                #    linewidth=0,
                #    background=colors[5],
                #),
                widget.TextBox(
                    #text="  ",
                    text="  ",
                    font="Iosevka Nerd Font",
                    fontsize="15",
                    background=colors[5],
                    foreground=colors[0],
                    padding=0,
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(os.path.expanduser("~/.config/sunset/scripts/launcher.sh"))
                    },
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=-3,
                    background=colors[5],
                    foreground=colors[0],
                ),
                widget.GroupBox(
                    font="Iosevka Nerd Font",
                    fontsize=13,
                    #margin_y=3,
                    #margin_x=6,
                    #padding_y=7,
                    #padding_x=-4,
                    padding=0,
                    spacing=2,
                    hide_unused=True,
                    borderwidth=4,
                    active=colors[1],
                    inactive=colors[2],
                    rounded=False,
                    highlight_color=colors[5],
                    urgent_alert_color=colors[6],
                    highlight_method="text",
                    urgent_alert_method="text",
                    this_current_screen_border=colors[5],
                    text_highlight_text_color=colors[0],
                    background=colors[0],
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=-3,
                    background=colors[0],
                    foreground=colors[0],
                ),
                #widget.Prompt(
                #    background=colors[2],
                #    foreground=colors[0],
                #    font="Iosevka Nerd Font",
                #    fontsize=18,
                #),
                #widget.Chord(
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),
                widget.Spacer(length=bar.STRETCH),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    scale=0.6,
                    background=colors[0],
                    foreground=colors[1],
                    padding=0,
                    font="Iosevka Nerd Font",
                    fontsize=14,
                ),
                widget.CurrentLayout(
                    font="Noto Sans Font",
                    fontsize=11,
                    margin_x=-20,
                    padding_y=-5,
                    background=colors[0],
                    foreground=colors[1],
                ),
                widget.TextBox(
                    text="\ue0ba",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=-1,
                    background=colors[0],
                    foreground=colors[5],
                ),
                 widget.TextBox(
                    text=" ",
                    font="Iosevka Nerd Font",
                    fontsize=14,
                    background=colors[5],
                    foreground=colors[0],
                    padding=0,
                ),
                widget.NvidiaSensors(
                    background=colors[5],
                    foregrond=colors[0],
                    metric=True,
                    update_interval=5,
                    font="Noto Sans",
                    fontsize=11,
                    threshold=70,
                    foreground_alert=colors[0],
                    foreground=colors[0],
                    format="{temp}°C",
                    padding=0,
                ),
                widget.TextBox(
                    text="\ue0ba",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=-1,
                    background=colors[5],
                    foreground=colors[3],
                ),
                widget.TextBox(
                    text=" ",
                    font="Iosevka Nerd Font",
                    fontsize=13,
                    background=colors[3],
                    foreground=colors[0],
                    padding=0,
                ),
                widget.NvidiaSensors(
                    background=colors[3],
                    foregrond=colors[0],
                    metric=True,
                    update_interval=5,
                    font="Noto Sans",
                    fontsize=11,
                    threshold=70,
                    foreground_alert="ffffff",
                    foreground=colors[0],
                    format="{fan_speed}",
                    padding=0,
                ),
                widget.TextBox(
                    text="\ue0ba",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=-1,
                    background=colors[3],
                    foreground=colors[5],
                ),
                widget.TextBox(
                    text=" ",
                    font="Iosevka Nerd Font",
                    fontsize=13,
                    background=colors[5],
                    foreground=colors[0],
                    padding=0,
                ),
                widget.ThermalSensor(
                    background=colors[5],
                    update_interval=5,
                    font="Noto Sans",
                    fontsize=11,
                    threshold=70,
                    foreground_alert="000000",
                    foreground=colors[0],
                    padding=0,
                ),
                widget.TextBox(
                    text="\ue0ba",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=-1,
                    background=colors[5],
                    foreground=colors[3],
                ),
                widget.TextBox(
                    text="墳 ",
                    font="Iosevka Nerd Font",
                    fontsize=13,
                    background=colors[3],
                    foreground=colors[0],
                    padding=0,
                ),
                widget.PulseVolume(
                    background=colors[3],
                    foreground=colors[0],
                    font="Noto Sans Font",
                    fontsize=11,
                    mouse_callbacks={
                        "Button3": lambda: qtile.cmd_spawn("kitty -e pulsemixer")
                    },
                    padding=0,
                ),
                # Doesn't work with Spotify so its disabled!
                # widget.TextBox(
                #    text="\u2572",
                #    font="Inconsolata for powerline",
                #    fontsize="33",
                #    padding=0,
                #    background=colors[13],
                #    foreground=colors[0],
                # ),
                # widget.Mpd2(
                #   background=colors[13],
                #   foreground=colors[0],
                #   idle_message=" ",
                #   idle_format="{idle_message} Not Playing",
                #   status_format="  {artist}/{title} [{updating_db}]",
                #   font="Iosevka Nerd Font",
                #   fontsize=15,
                # ),
                # This one works with Spotify, enable if you want!
                # widget.Mpris2(
                #    background=colors[13],
                #    foreground=colors[0],
                #    name="spotify",
                #    objname="org.mpris.MediaPlayer2.spotify",
                #    fmt="\u2572   {}",
                #    display_metadata=["xesam:title", "xesam:artist"],
                #    scroll_chars=20,
                #    font="Iosevka Nerd Font",
                #    fontsize=15,
                # ),
                widget.TextBox(
                    text="\ue0ba",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=-1,
                    background=colors[3],
                    foreground=colors[5],
                ),
                widget.TextBox(
                    text="   ",
                    font="Iosevka Nerd Font",
                    fontsize="12",
                    background=colors[5],
                    foreground=colors[0],
                    padding=-5,
                ),
                widget.Clock(
                    font="Noto Sans Font",
                    foreground=colors[0],
                    background=colors[5],
                    fontsize=11,
                    format="%a, %d %b",
                    padding=0,
                ),
                widget.TextBox(
                    text="\ue0ba",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=-1,
                    background=colors[5],
                    foreground=colors[3],
                ),
                widget.TextBox(
                    text=" ",
                    font="Iosevka Nerd Font",
                    fontsize="13",
                    padding=0,
                    background=colors[3],
                    foreground=colors[0],
                ),
                widget.Clock(
                    font="Noto Sans Font",
                    foreground=colors[0],
                    background=colors[3],
                    fontsize=11,
                    format="%H:%M",
                    padding=0,
                ),
                #widget.TextBox(
                #    text="\ue0ba",
                #    font="Inconsolata for powerline",
                #    fontsize="33",
                #    padding=0,
                #    background=colors[3],
                #    foreground=colors[5],
                #),
                widget.TextBox(
                    text="\ue0ba",
                    font="Inconsolata for powerline",
                    fontsize="33",
                    padding=-3,
                    background=colors[3],
                    foreground=colors[5],
                ),
                #widget.TextBox(
                #    text="\ue0ba",
                #    font="Inconsolata for powerline",
                #    fontsize="33",
                #    padding=-10,
                #    background=colors[5],
                #    foreground=colors[5],
                #),
                widget.TextBox(
                    #text="  ",
                    text="   ",
                    font="Iosevka Nerd Font",
                    fontsize="13",
                    padding=-1,
                    background=colors[5],
                    foreground=colors[0],
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(os.path.expanduser("~/.config/sunset/scripts/powermenu.sh"))
                    },
                ),
                #widget.Sep(
                #    padding=6,
                #    linewidth=0,
                #    background=colors[5],
                #),
            ],
            22,
            opacity=1,
            background=colors[0],
            margin=[6, 6, 0, 6],
        ),
        # left=bar.Gap(5),
        # right=bar.Gap(5),
    ),
]

# Helper functions #
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


# Mod + Mouse drag -> Floating
mouse = [
    Drag("M-1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag("M-3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click("M-2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        # default_float_rules include: utility, notification, toolbar, splash, dialog,
        # file_progress, confirm, download and error.
        *layout.Floating.default_float_rules,
        Match(title="Confirmation"),
        Match(title="Qalculate!"),
        Match(wm_class="OBS"),
        Match(wm_class="MultiMC"),
        Match(wm_class="Tilda"),
        #Match(wm_class="Steam"),
    ]
)


#@hook.subscribe.startup_once
#def start_once():
#    home = os.path.expanduser("~")
#    subprocess.call([home + "/.config/qtile/boot.sh"])

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])


# By default Spotify doesn't respect window rules, this is a fix.
@hook.subscribe.client_name_updated
def spotify(window):
    if window.name == 'Spotify':
        window.cmd_togroup(group_name='5')

def toscreen(qtile, group_name):
    if group_name  == qtile.current_screen.group.name:
        qtile.current_screen.set_group(qtile.current_screen.previous_group)
    else:
        for i in range(len(qtile.groups)):
            if group_name == qtile.groups[i].name:
                qtile.current_screen.set_group(qtile.groups[i])
                break


# back and forth feature
for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        #Key([mod], i.name, lazy.group[i.name].toscreen()),
        # switch to group with ability to go to prevous group if pressed again
        Key([mod], i.name, lazy.function(toscreen, i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])



