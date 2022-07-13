##
# @Author: Ed Ardolino
# @Version 1.5
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

# Boolean variables set to false, these will be used later to source the config files
upbash = False
upzsh = False
upfish = False


# Function to start the program and take user input
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

    # If statements to run the proper function based on the user input
    if response == "2":
        cronentry()

    # Asks the user if they would like to run the program again
    run_again()


# Writes to bash
def write_to_bash(string):
    with open(os.path.join((os.path.expanduser('~/.bashrc'))), "a") as file:
        file.writelines(str(string))
        file.write("\n")
        file.close()


# Writes to zsh
def write_to_zsh(string):
    with open(os.path.join((os.path.expanduser('~/.zshrc'))), "a") as file:
        file.writelines(str(string))
        file.write("\n")
        file.close()


# Writes to fish
def write_to_fish(string):
    with open(os.path.join((os.path.expanduser('~/.config/fish/config.fish'))), "a") as file:
        file.writelines(str(string))
        file.write("\n")
        file.close()


# Writes to crontab
# In order to allow you to write to a crontab, you will need to have an existing crontab file
# You will also need to add your user to the path below. Ex: '~/var/spool/cron/admin'
def write_to_cron(string):
    with open(os.path.join((os.path.expanduser('/var/spool/cron/'))), "a") as file:
        file.writelines(str(string))
        file.write("\n")
        file.close()


# Function to input an alias and write it to the alias file (bash)
def aliasbash():
    print("Please enter the alias you would like to add to ~/.bashrc:\n")
    print('Formt using the following syntax: alias up="sudo apt update && sudo apt upgrade -y"\n')
    print('Note: Make sure to include the double quotes ("") as the alias willl not function without them\n')
    bashresponse = input("Alias: ")
    write_to_bash(bashresponse)
    upbash = True


# Function to input an alias and write it to the alias file (bash)
def aliaszsh():
    print("Please enter the alias you would like to add to ~/.zshrc:\n")
    print('Format using the following syntax: alias up="sudo apt update && sudo apt upgrade -y"\n')
    print('Note: Make sure to include the double quotes ("") as the alias will not function without them\n')
    zshresponse = input("Alias: ")
    write_to_zsh(zshresponse)
    upzsh = True


# Function to input an alias and write it to the alias file (bash)
def aliashfish():
    print("Please enter the alias you would like to add to ~/.config/fish/config.fish:\n")
    print('Format using the following syntax: alias up="sudo apt update && sudo apt upgrade -y"\n')
    print('Note: Make sure to include the double quotes ("") as the alias will not function without them\n')
    fishresponse = input("Alias: ")
    write_to_fish(fishresponse)
    upfish = True


# Function to input the program and parameters into the crontab file (In progress)
# Writing to file successfully, but throwing errors after the fact
def cronentry():
    print("Please enter the parameters and program that you would like to add to the crontab file: \n")
    cronresponse = input("Cron: ")
    write_to_cron(cronresponse)


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
    if upfish:
        update_fish()
    exit(0)
