# Importing libraries
import sys

# Importing other files
import customfuncs
import game

class Menu:
    def __init__(self):
        try:
            menuoption = input("Welcome to my crappy card game! Please pick an option\n\n[0] Start Game\n[1] Options\n[2] Exit\n\n")
            if menuoption == "0":
                customfuncs.ClearConsole()
                Menu.JoinOptions()
            elif menuoption == "1":
                Menu.settings()
            elif menuoption == "2":
                customfuncs.ClearConsole()
                sys.exit()
        except KeyboardInterrupt:
            print("Woah woah woah woah")
    
    def settings():
        print("Not yet!")

    def JoinOptions():
        global joinip
        joinip = input("Enter the desired ip and port (please include https://): ")

        game.Game.join()