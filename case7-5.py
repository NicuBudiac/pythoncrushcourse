age = "\nWrite your age and I will tell you how much costs movie ticket"
age += "\nSo , enter your age : "
active = True
while active:
    ticket = int(input(age))
    if ticket < 3 :
        print("The ticket is free")
    elif ticket >= 3 and ticket <= 12:
        print("The ticket cost is 10$ ")
    elif ticket > 12 and ticket <=100:
        print("The ticket cost is 15$ ")
    else:
        active = False 
        print("Ilegal age , you are out of aplication")   