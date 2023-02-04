import string #allows to import characters in ascii and numbers with the digit
import random
passwordArg = string.ascii_letters + string.digits
password = []
def selector():
    selectedLength = int(input("Choose the length of your password : \n"))
    for i in range(selectedLength):
        password.append(random.choice(passwordArg))
        random.shuffle(password)
selector()
print(''.join(password))