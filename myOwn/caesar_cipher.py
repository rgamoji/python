def cipher(input,key):
    if not input.isalpha():
       return input
    output=""
    newOrd=0
    ord_z=ord('z')
    ord_Z=ord('Z')
    for char in input:
        if char == 'z':
          newOrd=ord('a') 
          print char,"Old:",ord(char),"New:",newOrd
          output+=chr(newOrd)
          continue
        elif char == 'Z':
          newOrd=ord('A') 
          print char,"Old:",ord(char),"New:",newOrd
          output+=chr(newOrd)
          continue
        if char.isupper():
           if ord(char)+key > ord_Z:
              newOrd=(ord(char)+key)-ord_Z+ord('A')-1
              print char,"Old:",ord(char),"New:",newOrd
              output+=chr(newOrd)
              #output+=chr(((ord(char)+key)-ord_Z)+ord('A')-1)
           else:
              newOrd=ord(char)+key
              print char,"Old:",ord(char),"New:",newOrd
              output+=chr(newOrd)
              #output+=chr(ord(char)+key)
        else:
           if ord(char)+key > ord_z:
              newOrd=(ord(char)+key)-ord_z+ord('a')-1
              print char,"Old:",ord(char),"New:",newOrd
              output+=chr(newOrd)
              #output+=chr(((ord(char)+key)-ord_z)+ord('a')-1)
           else:
              newOrd=ord(char)+key
              print char,"Old:",ord(char),"New:",newOrd
              output+=chr(newOrd)
              #output+=chr(ord(char)+key)
    
    return output

def decipher(input,key):
    output=""
    ord_z=ord('z')
    ord_Z=ord('Z')
    for char in input:
        if char == 'a':
          output+='z'
          continue
        elif char == 'A':
          output+='Z'
          continue
        print "",ord(char)-key
        output+=chr(ord(char)-key)
    return output
def main():
    input=raw_input("Enter a string: ")
    key=int(raw_input("Enter cipher key (1 to 25): "))
    cip=""
    for s in input.split(' '):
        cip+=cipher(s,key)
    print "Original:",input,"Key:",key,"Cipher:",cip
    decip=decipher(cip,key)
    print "Cipher:",cip,"Key:",key,"Original:",decip


if __name__ == '__main__':
   main()
