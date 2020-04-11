class Users():
    def __init__(self, first_name, last_name, age, ocupation, company):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.ocupation = ocupation
        self.company = company
        self.login_attempts = 0

    def describe_users(self):
        print("\t" + self.first_name.title() + " " + self.last_name.title() + " " + str(self.age) + " years"
                "\n\t" + "Is " + self.ocupation + " on " + self.company.title()
              )

    def greet_user(self):
        print("\n" + self.first_name.title() + " " + self.last_name.title() +
              " feel happy, you are successful people !!!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def read_login_attempts(self):
        print("Number of login attempts is : " + str(self.login_attempts))


user_1 = Users('nicu','budiac','25','working','gilat')
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.read_login_attempts())
user_1.reset_login_attempts()
print(user_1.read_login_attempts())



