import cs50
import sys

if len(sys.argv) != 2:
    print("Error") 
    exit(1)
else:
    k = int(sys.argv[1]);
    print("plaintext: ",end="")
    p = cs50.get_string();
    n = len(p)
    print("ciphertext: ",end="")
    for i in range (n):
        l = ord(p[i])
        m = l + (k % 26)
            
        if ((l>=97) and (l<=122)):
            if(m <= 122):
                print("{}".format(chr(m)),end="")
            else:
                print("{}".format(chr(m-26)),end="")
                
        elif ((l>=65) and (l <=90)):
            if(m <=90):
                print("{}".format(chr(m)),end="")
            else:
                print("{}".format(chr(m-26)),end="")
        
        else:
            print("{}".format(p[i]),end="")
    print()
