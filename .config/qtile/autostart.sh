#!/usr/bin/env bash

log_dir=$HOME/.local/share/qtile

_run_if_exist() {
  app_name=$(echo "$1" | awk '{ print $1 }')
  time=$(date +"%D %T")

  echo "[autostart] $time: Launch $app_name"
  $1 2>"$log_dir/$app_name.log" || echo "[warning] $" &
}

declare -a programs

programs=(
  "discord --no-sandbox"
  "nitrogen --restore"
  "redshift"
  "vivaldi-stable"
  "spotify"
)

for app in "${programs[@]}"; do
  _run_if_exist "$app"
done
