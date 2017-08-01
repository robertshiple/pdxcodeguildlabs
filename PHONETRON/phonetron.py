
"""
Kieran R Prasch

Phonebook Example Solution

"""

import sys
from secret import TWIL_SID, TWIL_TOKEN
from termcolor import colored, cprint
from twilio.rest import Client
from datetime import datetime


PHONEBOOK = list()


def welcome():
    banner = colored(f'''      {datetime.now()}    
    ****************************    
                                    
    WELCOME TO PPHONE TRON 6000     
        what do you want?           
                                    
    ****************************    ''', 'red', attrs=['reverse', 'blink'])
                    
    print(banner)                     


def add_contact(cmd):
        print('WUT CONTACT DO U WANT TO ADD??? ')
        name = input()
        print(' WUT IS THE PHONE NUMBER?')
        number = input()
        entry = {'name': name, 'number': number}    #add user dict with two key value pairs
        PHONEBOOK.append(entry)
        print(name + ' HAS BEEN ADDED')


def get_name(cmd):
        print(' WUT IS THE CONTACTS NAME? ')
        number = phonebook.get(name, 'no entry')
        print(name + ' -- ' + number)


def update_name(cmd):
        print('Name?')
        name = input()
        print('what do you want to update?')
        what_to_change = input()
        if what_to_change == 'name':
            print(' what do you want to change teh name tooooo??? ')
            new_name = input()
            
            for person in PHONEBOOK:       #linear search aka data finding 
                if person['name'] == name:
                    person['name'] = new_name
                    break

            print('kk its been updated')
        else:
            print('Unknown command: ' + cmd)

def list_names():
    print('                                     ')
    conbtacts = colored('*** HERES UR CURRENT COBNTACTS!!! ***', 'yellow', attrs=['reverse', 'blink'])
    print(conbtacts)
    print('                                     ') 
    for person in PHONEBOOK:  #looping over list
        for label in person:     #looping over dict
            print(person[label])   # printing the values of the keys

def message(cmd):
    print('                  ')
    print("MESSAGING CATS NOW")
    # Find these values at https://twilio.com/user/account
    account_sid = TWIL_SID
    auth_token = TWIL_TOKEN
    client = Client(account_sid, auth_token)

    message = client.api.account.messages.create(to="+19168380995",
                                             from_="+14243512633",
                                             body="HELLO THIS IS PHONE TRON.",
                                             media_url=[
                                                   'https://s-media-cache-ak0.pinimg.com/236x/02/a9/4b/02a94bea74be66e60aa7164505a4cf8c--its-funny-funny-shit.jpg',
                                                   ])




def menu():

    cmd = None
    while cmd != 'quit':
        cmd = input()
        if cmd == 'list':
           list_names()
        elif cmd == 'update':
            update_name(cmd)
        elif cmd == 'add':
            add_contact(cmd)
        elif cmd == 'cats':
            message(cmd)
        
      
if __name__ == '__main__':
    welcome()
    menu()