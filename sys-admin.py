#Introducing System Administration with Python

import os
import subprocess

os.system("ls")
subprocess.run(["ls","-l","README.md"])

#Retrieving system information

#The subprocess.run() function is powerful because you can use it to run any Bash command.
#In this exercise, you will call the uname command to get system information.
command="uname"
commandArgument="-a"

print(f'Gathering system information with command: {command} {commandArgument}')

subprocess.run([command,commandArgument])

#To emphasize that subprocess.run() allows you to run any command,
#you will run the df command to get disk information.
command="ps"
commandArgument="-x"

print(f'Gathering active process information with command: {command} {commandArgument}')

subprocess.run([command,commandArgument])
