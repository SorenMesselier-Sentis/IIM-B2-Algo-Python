import hashlib
mdp = input("What's the password you want to crack ? \n")

def brut_force():
    for i in range(0, 99999999):
        counter = str(i)
        password = hashlib.md5(counter.encode())
        verif = str(password.hexdigest())
        if verif == mdp:
            return print(f"The password is {i} and the md5 equals to : {verif}")
brut_force()