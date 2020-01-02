import re

def valid(password):
    if not len(password) >= 6 and len(password) <= 12:
        return False
    if not re.search("[a-z]",password):
        return False
    if not re.search("[0-9]",password):
        return False
    if not re.search("[A-Z]",password):
        return False
    if not re.search("[$#@]",password):
        return False
    return True

passwords = [password for password in input().split(",") if valid(password)]

print(",".join(passwords))
