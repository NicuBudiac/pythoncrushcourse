users = []
if users:    
    for user in users:
        print("Hello " + user.title() + ", would you like to see a status reports?")
else:
    print("We need to find some users!")
