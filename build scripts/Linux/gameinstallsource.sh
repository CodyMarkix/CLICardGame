#!/usr/bin/env bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

echo "Moving to /usr/local/bin..."

cd buildenv || return
sudo mv clicardgame /usr/local/bin/clicardgame

echo "Moved executable!"


echo "Final cleanup..."

cd ../ || return
rm -r buildenv

echo "Cleant up! Installation process finished!"