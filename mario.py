import cs50
while True:
    print("Height: ")
    h = cs50.get_int()
    if h >=0 and h <= 23:
        break
for i in range(h):
    for j in range(0,h-i-1):
        print(" ",end="")
    for k in range(i):
        print("#",end="")
    print("##")

        