polling_active = True
while polling_active:
    name = input("\nWhat is your name")
    response = input("Which mountain would you like to climb someday? ")
    
    classList = {}
    classList[name] = response
    
    repeat = input("Would you like to let another person respond ?(yes/no) ")
    if repeat == 'yes':
        polling_active = True
    else:
        polling_active = False
    
for name , response in classList.items():
    print(name.title() + "would you like to cilmb " + response.title() + " .")