import getpass
def checkpwd(pwd):
    spc = "\'\"\\!@#$%^&<>?|{}`~*():;.,/[-_=+`]"
    if len(pwd) < 8:
        print("Password must be at least 8 characters long.\n")
        return False
    elif not(any(char.isupper() for char in pwd)):
        print("Password must contain at least one uppercase character.\n")
        return False
    elif not(any(char.islower() for char in pwd)):
        print("Password must contain at least one lowercase character.\n")
        return False
    elif not(any(char in spc for char in pwd)):
        print("Password must contain at least one special character.\n")
        return False
    else:
        return True
def main():
    max_attempts = 5
    while max_attempts>0:
        passwd = getpass.getpass("Enter your password: ")
        conf = getpass.getpass("Re-enter your password: ")

        if passwd != conf:
            print("\nPasswords do not match. Please try again.\n")
            continue
        if checkpwd(passwd):
            print("\nPassword is strong.")
            break
        else:
            print("\nPlease try again.\n")
        max_attempts -= 1
    else:
        print("Maximum attempts reached. Please try again later.\n")
main()
