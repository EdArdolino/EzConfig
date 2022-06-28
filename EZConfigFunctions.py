##
# @Author: Ed Ardolino
# @Version 1.0
# @Creation Date: 6-28-2022
##

##
#
# ConfigureIt is a project that allows you to easily write changes to your *NIX config files
#
##

# Function to start the program and take user input
def start():
    print("\n Choose which config file you would like to update:\n 1.) Alias \n 2.) Chrontab")
    response  = input("Please enter a number from the list above:")
    while response not in {"1", "2"}:
            response = input("Invalid input, please enter a number from the list above")

    # If statement to take binary input and select the alias function
    if response == "1":
        print("\n Which shell are you using?:\n 1.) Bash \n 2.) Zsh \n 3.) Fish \n")
        shellresponse = input("Please enter a number from the list above:")
        while shellresponse not in {"1" , "2", "3"}:
                shellresponse = input("Invalid input, please enter a number from the list above.")

    if shellresponse == "1":
        aliasbash()

    if shellresponse == "2":
        aliaszsh()

    if shellresponse == "3":
        aliashfish()

    # If statement to take binary input and select the chrontab function
    if response == "2":
        chrontab()

    # Asks the user if they would like to run the program again
    #run_again()

# Writes to bash
def write_to_bash(string):
    with open ("~/.bashrc", "a") as file:
        file.writelines(str(string))

# Writes to zsh
def write_to_zsh(string):
    with open ("~/.zshrc", "a") as file:
        file.writelines(str(string))

# Writes to fish
def write_to_fish(string):
    with open ("~/.config/fish/config/fish") as file:
        file.writelines(str(string))

# Function to update the chrontab file
def chrontab():
    print("In progress")

# Function to input an alias and write it to the alias file (bash)
def aliasbash():
    print("Please enter the alias you would like to add to ~/.bashrc:\n")
    #bashresponse = input ()

# Function to input an alias and write it to the alias file (bash)
def aliaszsh():
    print("Please enter the alias you would like to add to ~/.zshrc:\n")

# Function to input an alias and write it to the alias file (bash)
def aliashfish():
    print("Please enter the alias you would like to add to ~/.config/fish/config.fish:\n")

