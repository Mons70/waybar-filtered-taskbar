#!/bin/bash

CONFIG_PATH="$HOME/.config/waybar/config"
# Start JSON array
echo "[" > $CONFIG_PATH

MODULES=""
# Loop through all active monitors and generate Waybar module configs
for mon in $(swaymsg -t get_outputs | jq -r '.[].name'); do
  echo "{
  \"layer\": \"top\",
  \"position\": \"top\",
  \"output\": \"$mon\",
  \"include\": \"~/.config/waybar/defconf\",
  \"modules-center\": [\"custom/taskbar-$mon\"],
  \"custom/taskbar-$mon\": {
    \"exec\": \"~/.config/waybar/scripts/taskbar.py $mon\",
    \"return-type\": \"json\"
  }
}," >> $CONFIG_PATH
done
sed -i '$ s/,$//' "$CONFIG_PATH"


echo "]" >> $CONFIG_PATH

# Restart Waybar to apply changes
pkill waybar && waybar &
