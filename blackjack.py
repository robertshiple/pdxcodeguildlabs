#ask user for three playing cards
#figure out the values of each card
# face cards are 10
#ace is 1 or 11 (only if it wont put the value over 21)
#lastly, figure out what the plying advice will be. use the following rules:
#print out the current total point value and advice
face = {'a':1, 'q':10, 'j':10, 'k':10, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10}


first = input("What's your first card?: ")
print(face[first])

second = input("What's your second card?: ")
print(face[second])

third = input("What's your third card?: ")
print(face[third])

total = face[first] + face[second] + face[third]

if total < 17:
    print("Hit")
elif total >= 17 and total < 21:
    print("Stay")
elif total == 21:
    print ("Blackjack!")
elif total > 21:
    print("busted!")


print(total)
