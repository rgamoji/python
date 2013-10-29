def return_series(until):
    count=0
    begin=0
    prev=0
    next=1
    series=[]
    while count < until: 
       next+=prev
       series.append(next)
       prev=begin
       begin=next 
       count += 1
    return series

count=int(raw_input("Enter the number of fibonacci numbers you want: "))
print return_series(count)
    
    

