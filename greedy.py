import cs50
#prompt the user for input
while True:
    print("O hai! How much change is owed?")
    f = cs50.get_float()
    if f > 0:
        break

c = round(f*100)
print(c)
q = c//25
q1=c%25
d=q1//10
d1=q1%10
n=d1//5
p=d1%5
  
s=q+d+n+p
print(s)
    