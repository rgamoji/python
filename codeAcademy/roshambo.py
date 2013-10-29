from random import randint
from sys import exit

def winner(human,comp):
    if human == 'Rock': 
       if comp == 'Paper':
          return comp
       elif comp == 'Scissors':
          return human
       else:
          return 'Draw'
    elif human == 'Paper':
       if comp == 'Scissors':
          return comp
       elif comp == 'Rock':
          return human
       else:
          return 'Draw'
    elif human == 'Scissors':
       if comp == 'Rock':
          return comp
       elif comp == 'Paper':
          return human
       else:
	  return 'Draw'

roshambo={1:'Rock',2:'Paper',3:'Scissors'}
my_choice=randint(1,3)
print roshambo[my_choice]
print "Welcome to Rock, Paper, Scissors!"
try:
    to_win=int(raw_input("How many points are required for win? "))
except:
    print "Are you kidding! I asked for a number."
    exit(1)
your_score=0
my_score=0

while your_score < to_win:
    try:
        human=raw_input("Choose (R)ock, (P)aper, or (S)cissors? ")
        if human.lower() == 'r':
           human='Rock'
        elif human.lower() == 'p':
           human='Paper'
        elif human.lower() == 's':
           human='Scissors'
        else:
           print 'Invalid Choice'
        comp=roshambo[randint(1,3)]
        result = winner(human,comp)
        if result != 'Draw':
            if result == human:
               print "\nYou chose: [",human,"] I chose:[",comp,"]\tYou Win!"
               your_score += 1
            else:
               print "\nYou chose: [",human,"] I chose:[",comp,"]\tI Win!"
               my_score +=1
        else:
           print "It's a ",result
    except EOFError:
           print "You chose to quit. That's fine. You donot win!"
	   exit(1)
    except KeyboardInterrupt:
           print "Well, that was a Ctrl-C, isn't it. That's fine. You donot win!"
           exit(1)
print "Final Score: You",your_score,"Me ",my_score
