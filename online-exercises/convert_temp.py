def convert(temp,type):
	target=0.0
	if (type.lower() == "f"):
		target = ((temp-32) * 5) / 9
		return target
	elif (type.lower() == "c"):
		target = 9 * temp / 5 + 32
		return target
	else:
		return 0

temp=float(raw_input("Enter a temparature: "))
type=raw_input("Convert to (F)arenheit or (C)elsius? ")
if type.lower() == "c":
	ttype="F"
else:
	ttype="C"	
print str(temp)+" "+type+" = "+str(convert(temp,type))+" "+ttype
