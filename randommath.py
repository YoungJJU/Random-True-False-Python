import random

a = random.randint(1,20)
b = random.randint(1,30)

print("a=",a,"b=",b)
x = input("a + b =?")
c = int(x)

if c == a + b:
    print("genius")
else:
    print("I'm so sorry but I love you")
