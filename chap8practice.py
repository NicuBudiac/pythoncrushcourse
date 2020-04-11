def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title()  + " !"
        print(msg)
username = ['hanah', 'ty', 'margot']
greet_users(username)