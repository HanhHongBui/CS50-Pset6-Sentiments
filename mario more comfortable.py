import cs50
while True:
    print("Height: ")
    h = cs50.get_int()
    if h >=0 and h <= 23:
        break
    
for i in range(1,h+1):
    print(" " *(h-i),end="")
    print("#"*i,end="")
    print("  ",end="")
    print("#"*i)