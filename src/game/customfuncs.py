import os

def ClearConsole():
    if os.name in ('nt', 'dos'):
        os.system("cls")
    else:
        os.system("clear")
