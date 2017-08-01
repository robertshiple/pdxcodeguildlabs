import string

"""

verify password:
at least 1 lowercase letter
at least 1 number
at least 1 uppercase letter
at least i special char
minimum length of 6 
max of 12!

"""

def validater():
    lower = False
    upper = False
    digits = False
    special = False

    print('Whats your password? ')
    password = input()
    if len(password) > 12:
        print('that password sucks')
    elif len(password) < 6:
        print('that password sucks')
    for c in password:
        if c in string.ascii_lowercase:
            lower = True
        elif c in string.ascii_uppercase:
            upper = True
        elif c in string.digits:
            digit = True
        elif c in password in ('@#$%^&*()_-+='):
            special = True
        if not all([lower, upper, digits, special]): #all takes iterables put bracktes around it!
            raise ValueError("nope")
    else:
        print('nice password!')

validater()
        