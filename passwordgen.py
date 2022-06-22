#Password generator
import time
import random
def createpassword():
    passwordlist = []
    for q in range(16):
            randomnum = random.randrange(33,126)
            asciipasword = chr(randomnum)
            asciipasswordstring = str(asciipasword)
            passwordlist.append(asciipasswordstring)
    print("Your Password is: ",*passwordlist , sep='')
    print("Your password is being automatically saved.")
    print("By the way, this file will be printed to wherever this python file is.")
    time.sleep(2)
    with open('passwords.txt', 'w') as f:
        f.writelines(["%s\n" % item  for item in passwordlist])
    print("Saved!")
    
def passwordgen():
    print("This will automaticly be a 16 digit password.")
    print("Starting now...")
    time.sleep(3)
    createpassword()
print("Hello and welcome to the ACME automatic password generator.")
time.sleep(2)
passwordgen()