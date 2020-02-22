prompt = "\nEnter a series of pizza toppings"
prompt += "\nIn case you want to exit from apication type 'quit'"

active = True
while active:
    toppings = input(prompt)

    if toppings == 'quit':
        active = False
    else:
        print("You just added following pizza topping: " + toppings + " !!!")