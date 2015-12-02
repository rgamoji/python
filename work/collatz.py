def compute_collatz(input):
    result=input
    step=0

    while result != 1:
        if result % 2 == 0:
           result = result / 2
        else:
           result = result * 3 + 1
        step += 1
    return step

def main():
    input=int(raw_input("Enter a number: "))
    print "According to Collatz Conjecuture, it takes:",compute_collatz(input),"steps to reduce",input,"to 1"


if __name__ == '__main__':
   main()
       
