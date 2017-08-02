
def winner(votes):  
    win = max(votes.items(), key=lambda t: t[1])
    return win



def vote():    
    votes = dict()
    while True:
        cmd = input('who do you vote for? ')
        if cmd == 'done':
            break
        else:
            name = str.lower(cmd)
            if name in votes: 
                votes[name] += 1    #if person is in dict already increment the value by one
            else:
                votes[name] = 1     #if new person
    print(votes)
    return votes

  
    
    
           
votes = vote()
the_winner = winner(votes)
name = the_winner[0]
number_of_votes = the_winner[1]
whatever = f'the winner is {name} with {number_of_votes} votes'
print(whatever)

        
