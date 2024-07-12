# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import re
import socket
import subprocess
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook
from libqtile import qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile.lazy import lazy
from libqtile.widget import Spacer
#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')
myTerm = "alacritty"

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.get_groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.get_groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.get_groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.get_groups[i + 1].name)

keys = [

# FUNCTION KEYS

   Key([], "F12", lazy.spawn('xfce4-terminal --drop-down')),

# SUPER + FUNCTION KEYS
    Key([mod], "e", lazy.spawn('emacs')),
    Key([mod], "c", lazy.spawn('conky-toggle')),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "m", lazy.spawn('pragha')),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "r", lazy.spawn('rofi-theme-selector')),
    Key([mod], "t", lazy.spawn("alacritty -e fish")),
    Key([mod], "a", lazy.spawn('code')),
    Key([mod], "d", lazy.spawn('discord')),
    Key([mod], "s", lazy.spawn('subl')),
    Key([mod], "v", lazy.spawn('pavucontrol')),
    Key([mod], "w", lazy.spawn('google-chrome-stable')),
    Key([mod], "b", lazy.spawn('brave')),
    Key([mod], "x", lazy.spawn('archlinux-logout')),
    Key([mod], "p", lazy.spawn('wpspdf')),
    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "Return", lazy.spawn("alacritty -e fish")),
    Key([mod], "KP_Enter", lazy.spawn("termite -e fish")),
    Key([mod], "F1", lazy.spawn('google-chrome-stable')),
    Key([mod], "F2", lazy.spawn('gvim')),
    Key([mod], "F3", lazy.spawn('inkscape')),
    Key([mod], "F4", lazy.spawn('gimp')),
    Key([mod], "F5", lazy.spawn('meld')),
    Key([mod], "F6", lazy.spawn('vlc --video-on-top')),
    Key([mod], "F7", lazy.spawn('virtualbox')),
    Key([mod], "F8", lazy.spawn('thunar')),
    Key([mod], "F9", lazy.spawn('evolution')),
    Key([mod], "F10", lazy.spawn("spotify")),
    Key([mod], "F11", lazy.spawn('rofi -show run -fullscreen')),
    Key([mod], "F12", lazy.spawn('rofi -show run')),

# SUPER + SHIFT KEYS

    Key([mod, "shift"], "Return", lazy.spawn('thunar')),
    Key([mod, "shift"], "d", lazy.spawn("dmenu_run -i -fn 'NotoMonoRegular:bold:pixelsize=15'")),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),
    #Key([mod, "shift"], "j", lazy.spawn('jgmenu_run')),

# CONTROL + ALT KEYS

    Key(["mod1", "control"], "Return", lazy.spawn('pcmanfm')),
    Key(["mod1", "control"], "d", lazy.spawn("dmenu_run -i -fn 'NotoMonoRegular:bold:pixelsize=15'")),
    Key(["mod1", "control"], "Prior", lazy.spawn('conky-rotate -p')),
    Key(["mod1", "control"], "a", lazy.spawn('xfce4-appfinder')),
    Key(["mod1", "control"], "c", lazy.spawn('catfish')),
    Key(["mod1", "control"], "e", lazy.spawn('archlinux-tweak-tool')),
    # Key(["mod1", "control"], "f", lazy.spawn('google-chrome-stable')),
    Key(["mod1", "control"], "g", lazy.spawn('google-chrome-stable')),
    Key(["mod1", "control"], "i", lazy.spawn('nitrogen')),
    Key(["mod1", "control"], "k", lazy.spawn('archlinux-logout')),
    Key(["mod1", "control"], "l", lazy.spawn('archlinux-logout')),
    Key(["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
    Key(["mod1", "control"], "p", lazy.spawn('pamac-manager')),
    Key(["mod1", "control"], "r", lazy.spawn('rofi-theme-selector')),
    Key(["mod1", "control"], "s", lazy.spawn('spotify')),
    Key(["mod1", "control"], "t", lazy.spawn("termite")),
    Key(["mod1", "control"], "u", lazy.spawn('pavucontrol')),
    Key(["mod1", "control"], "v", lazy.spawn('google-chrome-stable')),
    Key(["mod1", "control"], "w", lazy.spawn('arcolinux-welcome-app')),
    #Key(["mod1", "control"], "Return", lazy.spawn(myTerm+" -e fish")),
    Key(["mod1", "control"], "j", lazy.spawn('jgmenu_run')),
# ALT + ... KEYS

    Key(["mod1"], "f", lazy.spawn('variety -f')),
    Key(["mod1"], "h", lazy.spawn('xfce4-taskmanager')),
    Key(["mod1"], "n", lazy.spawn('variety -n')),
    Key(["mod1"], "p", lazy.spawn('variety -p')),
    Key(["mod1"], "t", lazy.spawn('variety -t')),
    # Key(["mod1"], "Up", lazy.spawn('variety --pause')),
    # Key(["mod1"], "Down", lazy.spawn('variety --resume')),
    # Key(["mod1"], "Left", lazy.spawn('variety -p')),
    # Key(["mod1"], "Right", lazy.spawn('variety -n')),
    Key(["mod1"], "F2", lazy.spawn('gmrun')),
    Key(["mod1"], "F3", lazy.spawn('xfce4-appfinder')),

# VARIETY KEYS WITH PYWAL

    Key(["mod1", "shift"], "f", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -f')),
    Key(["mod1", "shift"], "p", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -p')),
    Key(["mod1", "shift"], "n", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -n')),
    Key(["mod1", "shift"], "u", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -u')),

# CONTROL + SHIFT KEYS

    Key([mod2, "shift"], "Escape", lazy.spawn('xfce4-taskmanager')),

# SCREENSHOTS

    Key([], "Print", lazy.spawn("scrot 'ArcoLinux-%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'")),
    Key([mod2], "Print", lazy.spawn('xfce4-screenshooter')),
    Key([mod2, "shift"], "Print", lazy.spawn('gnome-screenshot -i')),

# MULTIMEDIA KEYS

# INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

# INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

#    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
#    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
#    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
#    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add_client(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add_client(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

# FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),]

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]

# FOR AZERTY KEYBOARDS
#group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

#group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
#group_labels = ["", "", "", "", "", "", "", "", "", "",]
group_labels = ["WWW", "DEV", "SYS", "DOC", "CHAT", "VID", "FILE", "IMG", "MUS",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])


# def init_layout_theme():
#     return {"margin":5,
#             "border_width":2,
#             "border_focus": "#5e81ac",
#             "border_normal": "#4c566a"
#             }

def init_layout_theme():
    return {"border_width": 2,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
            }

layout_theme = init_layout_theme()


layouts = [
    layout.MonadTall(**layout_theme),
    #layout.MonadWide(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 12,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 10,
         border_width = 2,
         bg_color = "1c1f24",
         active_bg = "c678dd",
         active_fg = "000000",
         inactive_bg = "a9a1e1",
         inactive_fg = "1c1f24",
         padding_left = 0,
         padding_x = 0,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 200
         ),
    layout.Floating(**layout_theme)
]

# COLORS FOR THE BAR

colors = [["#282c34", "#282c34"], # panel background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
          ["#e1acff", "#e1acff"], # window name
          ["#ecbbfb", "#ecbbfb"]] # backbround for inactive screens


# colors = init_colors()

##### MOUSE CALLBACKS #####

def open_taskmanager():
    qtile.spawn('xfce4-taskmanager')

def open_jgmenu():
    qtile.spawn('jgmenu_run')

def open_calendar():
    qtile.spawn('/home/raghhav/.config/qtile/scripts/calendar.sh')

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(
    font="Ubuntu Mono",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)


##### DEFAULT WIDGET SETTINGS #####
# widget_defaults = dict(
#     font="Ubuntu Mono",
#     fontsize = 12,
#     padding = 2,
#     background=colors[2]
# )
# extension_defaults = widget_defaults.copy()


widget.Prompt(
               prompt = prompt,
               font = "Ubuntu Mono",
               padding = 10,
               foreground = colors[3],
               background = colors[1]
               ),

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
               widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
               widget.Image(
                        filename = "~/.config/qtile/icons/python-white.png",
                        scale = "False",
                        mouse_callbacks = {'Button1': open_jgmenu}
                ),
             widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
               widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 11,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[7],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[6],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       background = colors[0]
                       ),
               widget.Prompt(
                       prompt = prompt,
                       font = "Ubuntu Mono",
                       padding = 10,
                       foreground = colors[3],
                       background = colors[1]
                       ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.WindowName(
                       font = "Ubuntu",
                       fontsize = 12,
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
               widget.Systray(
                       background = colors[0],
                       padding = 5
                       ),
               widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
               widget.TextBox(
                       font="FontAwesome",
                       text = '',
                       background = colors[0],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
               widget.Net(
                       interface = "wlo1",
                       # format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}'
                       font="Ubuntu",
                       fontsize=12,
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5
                       ),
               widget.TextBox(
                       font="FontAwesome",
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 37
                       ),
               widget.TextBox(
                       text = "",
                       padding = 2,
                       foreground = colors[2],
                       background = colors[5],
                       fontsize = 11
                       ),
               # widget.ThermalSensor(
               #  font="Ubuntu",
               #          fontsize=12,
               #         foreground = colors[2],
               #         background = colors[5],
               #         threshold = 90,
               #         padding = 5
               #         ),
               widget.Battery(
                        font="Ubuntu",
                        update_interval = 10,
                        fontsize = 12,
                        padding = 5,
                        format = "Battery: {percent:2.0%}",
                        low_foreground  = colors[2],
                        foreground = colors[2],
                        background = colors[5],
                        ),
               widget.TextBox(
                       font="FontAwesome",
                       text='',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " ⟳",
                       padding = 2,
                       foreground = colors[2],
                       background = colors[4],
                       fontsize = 14
                       ),
              widget.CheckUpdates(
                       update_interval = 60,
                       font="Ubuntu",
                        fontsize=12,
                       distro = "Arch_checkupdates",
                       display_format = "{updates} Updates",
                       foreground = colors[2],
                       mouse_callbacks = {'Button1': lambda: qtile.spawn(myTerm + ' -e sudo pacman -Syu')},
                       background = colors[4]
                       ),
               widget.TextBox(
                       font="FontAwesome",
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " 🖬",
                       foreground = colors[2],
                       background = colors[5],
                       padding = 0,
                       fontsize = 14
                       ),
               widget.Memory(
                font="Ubuntu",
                        fontsize=12,
                       foreground = colors[2],
                       background = colors[5],
                       mouse_callbacks = {'Button1': open_taskmanager},
                       padding = 5
                       ),
              widget.TextBox(
                       font="FontAwesome",
                       text='',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
               widget.TextBox(
                      text = " Vol:",
                      font="Ubuntu",
                        fontsize=12,
                       foreground = colors[2],
                       background = colors[4],
                       padding = 0
                       ),
              widget.Volume(
                font="Ubuntu",
                        fontsize=12,
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5
                       ),
               widget.TextBox(
                       font="FontAwesome",
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[0],
                       background = colors[5],
                       padding = 0,
                       scale = 0.7
                       ),
              widget.CurrentLayout(
                font="Ubuntu",
                        fontsize=12,
                       foreground = colors[2],
                       background = colors[5],
                       padding = 5
                       ),
              widget.TextBox(
                       font="FontAwesome",
                       text='',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Clock(
                        font="Ubuntu",
                        fontsize=12,
                       foreground = colors[2],
                       background = colors[4],
                       mouse_callbacks = {'Button1': open_calendar},
                       format = "%A, %B %d - %H:%M "
                       ),
              # widget.Tasklist(
              #           foreground = colors[2],
              #           background = colors[5],

              #          )
              ]
    return widgets_list


widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26))]
screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN

# @hook.subscribe.client_new
# def assign_app_group(client):
#     d = {}
#     #########################################################
#     ################ assgin apps to groups ##################
#     #########################################################
#     d["1"] = ["Navigator", "Firefox", 'google-chrome-stable", 'google-chrome-snapshot", "Chromium", "Google-chrome", "Brave", "Brave-browser",
#               "navigator", "firefox", 'google-chrome-stable", 'google-chrome-snapshot", "chromium", "google-chrome", "brave", "brave-browser", ]
#     d["2"] = [ "Atom", "Subl3", "Geany", "Brackets", "Code-oss", "Code", "TelegramDesktop", "Discord",
#                "atom", "subl3", "geany", "brackets", "code-oss", "code", "telegramDesktop", "discord", ]
#     d["3"] = ["Inkscape", "Nomacs", "Ristretto", "Nitrogen", "Feh",
#               "inkscape", "nomacs", "ristretto", "nitrogen", "feh", ]
#     d["4"] = ["Gimp", "gimp" ]
#     d["5"] = ["Meld", "meld", "org.gnome.meld" "org.gnome.Meld" ]
#     d["6"] = ["Vlc","vlc", "Mpv", "mpv" ]
#     d["7"] = ["VirtualBox Manager", "VirtualBox Machine", "Vmplayer",
#               "virtualbox manager", "virtualbox machine", "vmplayer", ]
#     d["8"] = ["Thunar", "Nemo", "Caja", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
#               "thunar", "nemo", "caja", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]
#     d["9"] = ["Evolution", "Geary", "Mail", "Thunderbird",
#               "evolution", "geary", "mail", "thunderbird" ]
#     d["0"] = ["Spotify", "Pragha", "Clementine", "Deadbeef", "Audacious",
#               "spotify", "pragha", "clementine", "deadbeef", "audacious" ]
#     ##########################################################
#     wm_class = client.window.get_wm_class()[0]
#
#     for i in range(len(d)):
#         if wm_class in list(d.values())[i]:
#             group = list(d.keys())[i]
#             client.togroup(group)
#             client.group.cmd_toscreen()

# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME



main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules, 
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='Arcolinux-welcome-app.py'),
    Match(wm_class='Arcolinux-tweak-tool.py'),
    Match(wm_class='Arcolinux-calamares-tool.py'),
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(wm_class='arcolinux-logout'),
    Match(wm_class='xfce4-terminal'),

],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
