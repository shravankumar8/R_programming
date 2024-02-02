import subprocess

# Define the commands
commands = [
    "cat /dev/null > ~/.bash_history",
    "history -c",
    "exit"
]

# Execute the commands one by one
for cmd in commands:
    subprocess.call(cmd, shell=True)
