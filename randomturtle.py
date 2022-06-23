import turtle as t
t.shape("turtle")
import random

t.speed(0)

for x in range(500):
    a = random.randint(1,360)
    t.setheading(a)
    b = random.randint(1,20)
    t.fd(b)

    
