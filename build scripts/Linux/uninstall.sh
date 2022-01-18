#!/usr/bin/env bash

if [ "$EUID" -ne 0 ]
  then echo "[ERROR] Please run as root (sudo ./uninstall)"
  exit
fi

echo "[...] Uninstalling..."

cd /usr/local/bin || return
sudo rm clicardgame

echo "[OK] Uninstalled!"