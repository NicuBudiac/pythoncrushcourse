users = ['admin', 'nickb', 'eugenp','viorelr', 'andreipa']
for user in users:
    if user == 'admin':
        print("Hello " + user.title() + ", would you like to see a status reports?")
    else:
        print("Hello " + user.title() + ", thank you for logging in again!!!")
