
def countdown(n):
    print ("Counting down from", n)
    count = 0
    while n >= 0:
        newvalue = (yield n)
        count += 1
        if count > 10 :
            return 1000
        # If a new value got sent in, reset n with it
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1

# The holy grail countdown
c = countdown(5)
for x in c:
    print(x)
    if x == 5:
        c.send(10)