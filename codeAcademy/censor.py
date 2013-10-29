def censor(line,word):
    string=line.split(' ')
    output=""
    for item in string:
        if item == word:
            item="".join("*"*len(word))
        output=output+" "+item
    return output.lstrip()

string= raw_input("Enter your string: ")
cen= raw_input("Enter what I should censor: ")

print censor(string,cen)
