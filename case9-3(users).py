class Users():
    def __init__(self,first_name, last_name, age,ocupation,company):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.ocupation = ocupation
        self.company = company



    def describe_users(self):
        print( "\t" + self.first_name.title() + " " + self.last_name.title() +  " " + str(self.age) + " years"
               "\n\t" + "Is " + self.ocupation + " on " +  self.company.title()
               )

    def greet_user(self):
        print("\n" + self.first_name.title() + " " + self.last_name.title() +
              " feel happy, you are successful people !!!")


user_1 = Users(input("Indroduce your first name"),input("Introduce your last name"),
               input("How many years are you"),input("What are you doing"),
               input("On witch company are you working"))
user_1.describe_users()
user_1.greet_user()

