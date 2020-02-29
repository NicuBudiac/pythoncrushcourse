def greet_users(names):
    for name in names:
        msg = "Hello, "+  name.title() + " !"
        print(msg)
user_name = ['hannah', 'ty', 'margot']
greet_users(user_name)