#!/usr/bin/env python3

# Importing libraries
import threading
import time

# Importing other python files
from flask import *
from mainmenu import Menu
import customfuncs

gamethread = threading.Thread(target=Menu)
time.sleep(1)
customfuncs.ClearConsole()
gamethread.start()