#!/usr/bin/env bash

FILE="$HOME/.config/polybar/blocks/scripts/rofi/colors.rasi"

# random accent color
#COLORS=('#cc6666' '#cc6666' '#b5bd68' '#b5bd68' '#f0c674' '#f0c674' '#81a2be' \
#		'#81a2be' '#b294bb' '#b294bb' '#8abeb7' '#8abeb7' '#b294bb' '#b5bd68')
#AC="${COLORS[$(( $RANDOM % 14 ))]}"
#sed -i -e "s/ac: .*/ac:   ${AC}FF;/g" $FILE
#sed -i -e "s/se: .*/se:   ${AC}FF;/g" $FILE

rofi -no-config -no-lazy-grab -show drun -modi drun -theme ~/.config/polybar/blocks/scripts/rofi/launcher.rasi
