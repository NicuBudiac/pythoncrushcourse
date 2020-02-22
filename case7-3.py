number = input("Tell me a number and I tell you if number is multiple of 10 \nSo tell me your number: ")
number = int(number)
if number % 10 == 0:
    print(str(number) + " is multiple of 10")
else:
    print(str(number) + " is not multiple of 10")