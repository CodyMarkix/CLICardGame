# CLI card game

A card game, definetly not based on UNO ;)

# How to play:

This game can only be played with **4 players**. (3 and less coming soon!)

Each player gets 7 cards at the start of the game. These include:

## Normal cards:
- "1" card
- "2" card
- "3" card
- "4" card
- "5" card
- "6" card
- "8" card
- "9" card

## Special cards:
- "0" card - shuffles the hands along the current direction
- "7" card - the person who plays the card has to swap hands with the person of their choice
- "skip card" - skips the next player's turn
- "reverse card" - reverse the game direction

To win, you need to have no cards remaining. When you have a single card remaining, you have to yell "UNO!" (press U to yell).

# Installing:

## Windows:

Download the latest release from the release tab. 

Your antivirus/Windows defender may throw a hissy fit, as the executable is not signed with a certificate. (I can't afford one 😅)

Simply move the downloaded executable to somewhere you'd like, left-click the executable and you're laughing!

## macOS:

You unfortunately have to build a binary yourself. 

Skip to "Build from source".

## Linux:

**AppImage coming soon!**

For now, this game utilizes an install script. In the releases tab is an archive called `Clicardgame.tar`.

Download the archive and extract it. This can either be done with your distribution's file manager or with the terminal, using:
```
tar -xvf Clicardgame.tar
```

Open the extracted archive and make `install.sh` executable:
```
chmod +x gameinstall.sh
```

And install the game:
```
sudo ./install.sh
```


# Building from source:

## Requirements:

### Programs:
- Python 3.x (Not sure about 3.10)
- Pyinstaller

### Python modules:
- Flask

# To-Do list:

- [x] Basic main menu
- [] Server Backend
- [] Game logic

### Things I cannot really promise but will potentionally be added later!:

- [] Leaderboards
- [] Quick play