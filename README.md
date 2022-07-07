\# **EZConfig**

About: This is a python program to easily turn user input into changes in the selected config file

Functionality: Easily add/update config files.


How to use:

1. Clone EZConfig into a directory of your choosing
2. Open a Windows Powershell or Windows Command Prompt in the directory of EZConfig.py
3. Enter 'python EZConfig.py' in the command line
   1. Note: If program does not run properly, use `sudo python EZConfig.py`
4. Example: `'C:\Users\Admin\Documents\Python\EZConfig' python EZConfig.py`
5. You will be prompted to select an option from the list, Alias or Crontab
6. Next, you will be asked to enter your desired alias/crontab
7. Once you have entered the arguments you would like to update, you will be asked if you would like to run the program again
8. All config files will automatically be reloaded upon exit of the program

Note: If your config files are not updated, you can manually update them using for following command(s) based on your shell: `source ~/.bashrc`, `source ~/.zshrc`, `source ~/.config/fish/config.fish`
Note (write_to_cron): In order to allow you to write to a crontab, you will need to have an existing crontab file (`creontab -e`). You will also need to add your user to the path. Ex: `~/var/spool/cron/admin` 

In Progress:
1. Writing to crontab
2. Input sanitization
	1. New lines added to end of all files, making sure input stays separated
