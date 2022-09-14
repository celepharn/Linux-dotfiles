#!/bin/bash

# You can call this script like this:
# $./volume.sh up
# $./volume.sh down
# $./volume.sh mute

# icons
audioicon=audio-volume-high
muteicon=audio-volume-muted

function get_volume {
    amixer get Master | grep '%' | head -n 1 | cut -d '[' -f 2 | cut -d '%' -f 1
}

function is_mute {
    amixer get Master | grep '%' | grep -oE '[^ ]+$' | grep off > /dev/null
}

function send_notification {
    volume=`get_volume`
    # Make the bar with the special character ─ (it's not dash -)
    # https://en.wikipedia.org/wiki/Box-drawing_character
    # bar=$(seq -s "─" $(($volume / 5)) | sed 's/[0-9]//g')
    # Send the notification
    dunstify -i $audioicon -t 1600 -r 2593 -h string:x-dunst-stack-tag:volume  -u normal "Volume $volume%" -h int:value:$volume
}

case $1 in
    up)
	# Set the volume on (if it was muted)
	amixer -q -D pulse set Master on > /dev/null
	# Up the volume (+ 5%)
	amixer -q -D pulse sset Master 5%+ > /dev/null
	send_notification
	;;
    down)
	amixer -q -D pulse set Master on > /dev/null
	amixer -q -D pulse sset Master 5%- > /dev/null
	send_notification
	;;
    mute)
    	# Toggle mute
	amixer -q -D pulse set Master 1+ toggle > /dev/null
	if is_mute ; then
		dunstify -i $muteicon -t 1600 -r 2593 -h string:x-dunst-stack-tag:volume -u normal "muted :)"
	else
	    send_notification
	fi
	;;
esac

