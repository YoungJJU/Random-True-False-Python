import time
input("press enter to start counting")
start = time.time()

input("press enter to end counting 20seconds")
end = time.time()

et = end - start

print("my countings", et, "seconds")
print("differences", abs(et - 20), "seconds")
