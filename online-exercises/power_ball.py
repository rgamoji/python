from random import choice,randint

print "Official (but fruitless) Powerball number generator"

sets=int(raw_input("How many sets of numbers: "))

count=0
seq=[]
pwr_bl=0
while count < sets:
    num=0
    for rand in range(1,6):
        num=choice(range(1,70))
        if num not in seq:
           seq.append(num)
	else:
           num=0
           while num not in seq:
              num=choice(range(1,70))
              seq.append(num)
             
    pwr_bl=choice(range(1,27))
    print "You numbers: ",
    for num in seq:
       print num,
    print "Powerball:",pwr_bl
    count+=1
    seq=[]
print ""

	
