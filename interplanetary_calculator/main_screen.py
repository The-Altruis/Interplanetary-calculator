import hohmann
import bi_elliptic
import sys
import os
import platform
import time
import subprocess

print("Version 1.3.8")

def auto_updates():
    print("Please wait, checking for updates...")
    try:
        subprocess.run(["git", "fetch", "origin"], check=True, stdout=subprocess.DEVNULL)
        local_commit = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip()
        remote_commit = subprocess.check_output(["git", "rev-parse", "origin/main"]).strip()
        if local_commit != remote_commit:
            update = input("An update is avalible, would you like to proceed? [Y/N] ").strip().lower()
            if update == "yes":
                print("Updating...")
                subprocess.run(["git", "pull", "origin", "main"], check=True)
                print("Update success.")
            else:
                print("Understood.")
        else:
            print("All is up-to-date.")
    except subprocess.CalledProcessError:
        print("I appologize, I could not connect to Github. Skipping Update.")


def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

#This is the main screen, you will enter which calculator you want to use, and you type in "exit" if you want to stop the program
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

auto_updates()
choice()