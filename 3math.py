import random

for x in range(1,4):
    a = random.randint(1,20)
    b = random.randint(1,30)
    if x == 1:
        print("a=",a,"b=",b)
        s = input("a + b =")
        c = int(s)
        if c == a +b:
            print("genius")
        else:
            print("sorry")

    if x == 2:
        print("a=",a,"b=",b)
        s = input("a + b =")
        c = int(s)
        if c == a +b:
            print("genius")
        else:
            print("sorry")

    if x == 3:
        print("a=",a,"b=",b)
        s = input("a + b =")
        c = int(s)
        if c == a +b:
            print("genius")
        else:
            print("sorry")
