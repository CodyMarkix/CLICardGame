#!/usr/bin/env bash

echo "[...] cd'ing into root project folder..."

cd ../../ || return

echo "[OK] cd'ed into root project folder!"


echo "[...] Creating neccesary directories..."

mkdir buildenv
cd buildenv || return

echo "[OK] Created neccesary directories!"


echo "[...] Building binary..."

~/.local/bin/pyinstaller --onefile ../src/game/main.py ../src/game/mainmenu.py ../src/game/game.py

echo "[OK] Built binary!"


echo "[...] Removing unneccesary files..."

cd dist || return
mv ./* ../
cd .. || return
rm -r dist
rm -r build
rm -r main.spec
mv main clicardgame

echo "[OK] Files removed!"


echo ""
echo "Please run ./install as root. (sudo ./install)"