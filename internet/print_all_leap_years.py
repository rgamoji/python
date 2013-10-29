def get_leap_years(limits):
    leap_year=[]
    for year in limits:
        if year % 4 == 0:
            if year % 100 == 0:
               if year % 400 == 0:
                  leap_year.append(year)
            else:
               leap_year.append(year)
    return leap_year

yearStart=int(raw_input("Enter Start Year: "))
yearEnd=int(raw_input("Enter End Year: "))

limits=range(yearStart,yearEnd+1,1)
all_leap_years=get_leap_years(limits)
print "List of Leap Years in your input range "+str(yearStart)+" and "+str(yearEnd)
for year in all_leap_years:
    print str(year)
