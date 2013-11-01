def cipher(input,key,reverse=False):
    output=""
    for char in input:
        if char == ' ' or not char.isalpha():
           output+=char
           continue
        if not char.isupper():
           output+=chr(transform(char,key,reverse))
        else:
           char=chr(ord(char)+32)
           output+=chr(transform(char,key,reverse)-32)
    return output

def transform(char,key,reverse=False):
    val_c=0
    if not reverse:
        val_c=ord(char)+key
    else:
        val_c=ord(char)-key
    if 97 <= val_c <= 122:
       return val_c
    else:
       return (96 + abs(val_c - 122))

def main():
    input=raw_input("Enter a string: ")
    key=int(raw_input("Enter cipher key (1 to 25): "))
    cip=cipher(input,key)
    print "Original:",input,"Key:",key,"Cipher:",cip
    input=cipher(cip,key,True)
    print "Cipher:",cip,"Key:",key,"Original:",input
    


if __name__ == '__main__':
   main()
