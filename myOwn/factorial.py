def factorial(input):
    if input == 0:
        return 1
    else:
        return input*factorial(input - 1)
    
print str(factorial(20))
