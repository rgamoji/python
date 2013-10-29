from random import choice,randint

print "Official (but fruitless) Powerball number generator"

sets=int(raw_input("How many sets of numbers: "))

count=0
seq=[]
pwr_bl=0
while count < sets:
    for rand in range(1,7):
        seq.append(choice(range(0,54)))
    pwr_bl=choice(range(0,43))
    print "You numbers: ",
    for num in seq:
       print num,
    print "Powerball:",pwr_bl
    count+=1
    seq=[]
print ""

	
