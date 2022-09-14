#!/bin/bash

# You can call this script like this:
# $./brightness.sh up
# $./brightness.sh down

# icon
brightnessicon=brightnesssettings

function get_brightness {
    light | grep -oE '^[0-9]+'
}

function send_notification {
    brightness=`get_brightness`
   # Send the notification
    dunstify -i $brightnessicon -t 1600 -h string:x-dunst-stack-tag:brightness -u normal "Brightness $brightness%" -h int:value:"$brightness"
}

case $1 in
    up)
	brightnessctl s 5+ > /dev/null
	send_notification
	;;
    down)
	brightnessctl s 5- > /dev/null
	send_notification
	;;
esac

