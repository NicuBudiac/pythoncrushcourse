start = 11
numbers = [3,6,14,2,7,42,15,19]
for val in numbers:
    if val > 1:
        for n in range (2,val):
            if (val % n) == 0:
                break
        else:
            print(val)