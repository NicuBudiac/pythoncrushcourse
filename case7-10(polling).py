active_polling = True
while active_polling:
    user_name = input("\nWhats your name :")
    vacation_location = input("Where do you want to spent your vacantion: ")

    # Declaring an empty dictionary to store user imput
    user_input = {}
    # Storing user inputs
    user_input[user_name] = vacation_location

    repeat =  input("\nWould you like to respond another person (yes/no) ")
    if repeat == 'yes':
        active_polling = True
    else:
        active_polling = False

for user_name, vacation_location in user_input.items():
    print(user_name.title() + "want to visit " + vacation_location.title() + " .")
