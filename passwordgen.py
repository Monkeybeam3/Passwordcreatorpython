#Password generator
import sys
import time
import random
def looppassword():
    print("Making some more passwords... These will all be charecter passwords...")
    original_stdout = sys.stdout
    passwordlistf = []
    for i in range(48):
            randomnum = random.randrange(33,126)
            asciipasword = chr(randomnum)
            asciipasswordstring = str(asciipasword)
            passwordlistf.append(asciipasswordstring)
    with open('passwords.txt', 'a') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(*passwordlistf , sep='')
        sys.stdout = original_stdout
    looppassword()
def createpassword():
    howlong = input("How many charecters should the password be? (in number form please): ")
    howlongint = int(howlong)
    original_stdout = sys.stdout
    passwordlist = []
    for q in range(howlongint):
            randomnum = random.randrange(33,126)
            asciipasword = chr(randomnum)
            asciipasswordstring = str(asciipasword)
            passwordlist.append(asciipasswordstring)
    print("Your password is " , *passwordlist , sep='')
    time.sleep(2)
    print("Your password is being automatically saved to a file called passwords.txt.")
    time.sleep(2)
    print("By the way, this file will be printed to wherever this python file is.")
    time.sleep(2)      
    with open('passwords.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(*passwordlist , sep='')
        sys.stdout = original_stdout
    print("Saved!")
    again = input("Would you like to create more passwords? (Y/n): ")
    if again == "Y" or "y":
        print("Ok!")
        looppassword()
    elif again == "N" or "n":
        print("Goodbye!")
    elif again != "Y" or "y" or "N" or "n":
        print("Automaticly creating a new password...")
def passwordgen():
    print("This will automaticly create a password.")
    print("Starting now...")
    time.sleep(3)
    createpassword()
print("Hello and welcome to the ACME automatic password generator.")
time.sleep(2)
createpassword()
#REMEMBER TO CHANGE THIS