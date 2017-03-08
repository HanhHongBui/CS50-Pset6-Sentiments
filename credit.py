import cs50

#prompt for input
print("Number: ",end="")
cardnum = cs50.get_int()

n = len(str(cardnum))
if n!=13 and n!=15 and n!=16:
    print("INVALID")
    
else:
    cardnumodd= cardnum
    cardnumeven=cardnum//10
    count = 0
    
    cardnum1 = []
    cardnum2 = []
    cardnum_multiply=[]
    
    #sum of odd digits
    for i in range (0,(n+1)//2):
        cardnum1.insert(i,cardnumodd%10)
        cardnumodd=cardnumodd//100
        #print("odd: {}".format(cardnum1[i]))
    s_odd = sum(cardnum1)
    #print("s odd: {}".format(s_odd))
    
    #sum of other digits, x2
    for j in range (0,(n//2)):
        cardnum2.insert(j,cardnumeven%10)
        cardnumeven=cardnumeven//100
        #print("even: {}".format(cardnum2[j]))
    cardnum_multiply=[2*x for x in cardnum2]
    for k in range (0,n//2):
        #print("x2: {}".format(cardnum_multiply[k]))
        if cardnum_multiply[k] >= 10:
            cardnum_multiply[k] = (cardnum_multiply[k])%10
            count = count+1
    s_even = count + sum(cardnum_multiply)
    s = s_odd + s_even
    smod = s%10
    #print("s even: {}".format(s_even))
    #print("s: {}".format(s))
    
    #check brands
    cardnumstr=str(cardnum)
    
    if (n == 13 or n == 16) and cardnumstr[0] == '4' and smod==0:
        print("VISA")
    elif n == 15 and cardnumstr[0] == '3' and (cardnumstr[1] =='4' or cardnumstr[1] =='7') and smod==0  :
        print("AMEX")
    elif n == 16 and cardnumstr[0]== '5' and (int(cardnumstr[1]) in range(0,6)) and smod==0:
        print("MASTERCARD")
    else:
        print("INVALID")
        
        