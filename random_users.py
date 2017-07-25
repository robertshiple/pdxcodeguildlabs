from datetime import datetime
import requests


r = requests.get('http://api.randomuser.me/?results=5') # pull a HTTP request!
data = r.json()

for person in data['results']:

    date = datetime.strptime(person['dob'], '%Y-%m-%d %H:%M:%S') #convert date tables
    nice_date = datetime.strftime(date, '%x')

    register = datetime.strptime(person['registered'], '%Y-%m-%d %H:%M:%S')
    registers = datetime.strftime(register, '%x')
    
    name = person['name'] #loop through dict to grab values 
    for key in name:
        print(name[key])

    print(person['email'])
    print(nice_date)
    print(registers)