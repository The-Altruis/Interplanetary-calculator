import hohmann
import bi_elliptic
import sys
import os
import platform
import time
print("Version 1.2.9")

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def choice():
    while True:
        print(" ")
        what_calculator = input("What calculator would you like to use? Hohmann or Bi-Elliptic, or would you like to Exit? ").strip().lower()
        if what_calculator == "hohmann":
            print("Launching...\n")
            time.sleep(5)
            hohmann.hohmann_transfer_calculator()
            input("Press Enter to return to the menu...")
            clear_console()
        elif what_calculator == "bi-elliptic":
            print("Launching...\n")
            time.sleep(5)
            bi_elliptic.bi_elliptic_transfer_calculator()
            input("Press Enter to return to the menu...")
            clear_console()
        elif what_calculator == "exit":
            print(" ")
            print("Understood. Enjoy your day.")
            sys.exit()
        else:
            print(" ")
            print("I'm sorry, that is not a suitable answer.")
choice()


#To-do list for later versions:
# - add a code that calculates a transfer from planet to moon, or planet to planet, then too moon.
# - add inclnation code.
# - update the code when needed.
# - make 3D model.
# - add survivability equation.
# - add a code that logs the outputs.
# - after all of this, add a GUI to make the console and UI easier for people to use.