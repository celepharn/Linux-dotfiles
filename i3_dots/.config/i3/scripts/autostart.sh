#!/bin/bash

function run {
	if ! pgrep $1;
	then
		$@&
	fi
}

run caffeine &
run xmodmap ~/.Xmodmap &
unclutter --timeout 3 --start-hidden &
#run xfce4-power-manager &
