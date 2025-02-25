#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#Set your native resolution IF it does not exist in xrandr
#More info in the script
#run $HOME/.config/qtile/scripts/set-screen-resolution-in-virtualbox.sh

#Find out your monitor name with xrandr or arandr (save and you get this line)
#xrandr --output VGA-1 --primary --mode 1360x768 --pos 0x0 --rotate normal
#xrandr --output DP2 --primary --mode 1920x1080 --rate 60.00 --output LVDS1 --off &
#xrandr --output LVDS1 --mode 1366x768 --output DP3 --mode 1920x1080 --right-of LVDS1
#xrandr --output HDMI2 --mode 1920x1080 --pos 1920x0 --rotate normal --output HDMI1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output VIRTUAL1 --off

#change your keyboard if you need it
#setxkbmap -layout be

#autostart ArcoLinux Welcome App
#run dex $HOME/.config/autostart/arcolinux-welcome-app.desktop &

#Some ways to set your wallpaper besides variety or nitrogen
#start the conky to learn the shortcuts
nitrogen --restore &
(conky -c $HOME/.config/qtile/scripts/system-overview) &


#starting utility applications at boot time
run nm-applet &
run pamac-tray &
run xfce4-power-manager &
picom --config $HOME/.config/qtile/scripts/picom.conf &
/usr/bin/emacs --daemon &
redshift -O 3000
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
sudo rm -r  ~/.config/qtile/archive/
#starting user applications at boot time
run volumeicon &
run imwheel &
run blueberry-tray&
#run discord &
#nitrogen --restore &
#run caffeine -a &
#run vivaldi-stable &
#run firefox &
#run thunar &
#run dropbox &
#run insync start &
#run spotify &
#run atom &
#run telegram-desktop &
