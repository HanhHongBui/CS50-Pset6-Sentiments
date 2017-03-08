import cs50
import sys


if len(sys.argv) != 2:
    print("Error") 
    exit(1)
else:   
    #check if key is letter
    
    key = sys.argv[1]
    lenk = len(key)
    
    for k in range(lenk):
        if (key[k].isalpha() == False):
            print("Error") 
            exit(1)
    
    print("plaintext: ",end="")
    p = cs50.get_string()
    print("ciphertext: ",end="")
    
    lenp = len(p)
    #set a counter
    kalpha = 0 
   
    for i in range(lenp):
        if (p[i].isalpha() == True):
            l = ord(p[i])
            s = kalpha%lenk
            j = ord(key[s])
            m1 = l + j -65
            m2 = l + j -97
                
            #p[i] is capital
            if ((l>=65) and (l<=90)):
                
                #key is capital
                if((j >=65) and (j<=90)):
                    if(m1 <=90):
                        print("{}".format(chr(m1)),end="")
                    else:
                        print("{}".format(chr(m1-26)),end="")
                        
                #key is lower case
                if((j >=97) and (j<=122)):
                    if(m2 <=90):
                        print("{}".format(chr(m2)),end="")
                    else:
                        print("{}".format(chr(m2-26)),end="")
                
            #p[i] is lower case
            else:
                if((j >=65) and (j<=90)):
                    if(m1 <=122):
                        print("{}".format(chr(m1)),end="")
                    else:
                        print("{}".format(chr(m1-26)),end="")
                    
                if((j >=97) and(j<=122)):
                
                    if(m2 <=122):
                        print("{}".format(chr(m2)),end="")
                    else:
                        print("{}".format(chr(m2-26)),end="")
                
            kalpha = kalpha +1
                
        else:
            print("{}".format(p[i]),end="")
    print()    
