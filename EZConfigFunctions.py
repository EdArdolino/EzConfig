##
# @Author: Ed Ardolino
# @Version 1.0
# @Creation Date: 6-28-2022
##

##
#
# EZConfig is a project that allows you to easily write changes to your *NIX config files
#
##

# Function to start the program and take user input
import os
import subprocess

upbash = False
upzsh = False
upfish = False


def start():
    print("\n Choose which config file you would like to update:\n 1.) Alias \n 2.) Crontab")
    response = input("Please enter a number from the list above:")
    while response not in {"1", "2"}:
        response = input("Invalid input, please enter a number from the list above")

    # If statement to take binary input and select the alias function
    if response == "1":
        print("\n Which shell are you using?:\n 1.) Bash \n 2.) Zsh \n 3.) Fish \n")
        shellresponse = input("Please enter a number from the list above:")
        while shellresponse not in {"1", "2", "3"}:
            shellresponse = input("Invalid input, please enter a number from the list above.")

    if shellresponse == "1":
        aliasbash()

    if shellresponse == "2":
        aliaszsh()

    if shellresponse == "3":
        aliashfish()

    # If statement to take binary input and select the crontab function
    if response == "2":
        crontab()

    # Asks the user if they would like to run the program again
    run_again()


# Writes to bash
def write_to_bash(string):
    with open(os.path.join((os.path.expanduser('~/.bashrc'))), "a") as file:
        file.writelines(str(string))
        print(string)

# Writes to zsh
def write_to_zsh(string):
    with open(os.path.join((os.path.expanduser('~/.zshrc'))), "a") as file:
        file.writelines(str(string))
        file.close()


# Writes to fish
def write_to_fish(string):
    with open(os.path.join((os.path.expanduser('~/.config/fish/config.fish'))), "a") as file:
        file.writelines(str(string))
        file.close()

# Function to update the crontab file
def crontab():
    print("In progress")


# Function to input an alias and write it to the alias file (bash)
def aliasbash():
    print("Please enter the alias you would like to add to ~/.bashrc:\n")
    bashresponse = input("Alias: ")
    write_to_bash(bashresponse)
    upbash = True


# Function to input an alias and write it to the alias file (bash)
def aliaszsh():
    print("Please enter the alias you would like to add to ~/.zshrc:\n")
    zshresponse = input("Alias: ")
    write_to_zsh(zshresponse)
    upzsh = True

# Function to input an alias and write it to the alias file (bash)
def aliashfish():
    print("Please enter the alias you would like to add to ~/.config/fish/config.fish:\n")
    fishresponse = input("Alias: ")
    write_to_fish(fishresponse)
    upfish = True

# Function to source ~/.bashrc
def update_bash():
    subprocess.run(["source", "~/.bashrc"])

# Function to source ~/.zshrc
def update_zsh():
    subprocess.run(["source", "~/.zshrc"])

# Function to source ~/.config/fish/config.fish
def update_fish():
    subprocess.run(["source", "~/.config/fish/config.fish"])

# Function to run the program again
def run_again():
    add_more = input("\n Would you like to run EZConfig.py again? (y/n): ").lower()
    while add_more not in {"y", "n"}:
        add_more = input("Incorrect input, please enter y or n: ")

    # If statement to either run the program again or terminate
    if add_more == "y":
        start()
    elif "n":
        print("\n Thank you. \n")
        # If statements to source config files
        if upbash:
            update_bash()
        if upzsh:
            update_zsh()
        if upfish():
            update_fish()
        exit(0)
