def interest(principal, rate, period):
    interest=0.00
    principal_in_cents=principal*100
    interest=principal_in_cents * (rate/100) * period
    return interest
def emi(amount,period):
    amount = amount * 100
    months = period * 12
    emi=float(amount / months)
    print emi
    return emi 
def print_schedule(amount,apr,period):
    reminder=amount
    sched=0
    while sched <= period*12:
        if sched > 0:
           reminder=reminder-apr
        print sched,apr,reminder
	sched+=1
    
pr=float(raw_input("Amount borrowed: "))
rt=float(raw_input("Interest rate: "))
tm=float(raw_input("Term (years): "))
intr=float(interest(pr,rt,tm) / 100)
total=intr+pr
apr=float(emi(total,tm) / 100)
apr=round(apr,2)
print_schedule(total,apr,tm)
