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

class Admin(Users):
    def __init__(self,first_name, last_name,age ,ocupation,company):
        super().__init__(first_name,last_name,age,ocupation,company)
        self.privileges = Privileges()


class Privileges():
    def __init__(self, privileges = ['can add post','can delete post','can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        for i in self.privileges:
            print(i)

user = Admin('nicu','budiac','35','working','gilat')
user.privileges.show_privileges()