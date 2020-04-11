class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 20

    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name.title() + " !")
        print("Type of cuisine is " + self.cuisine_type.title() + " .")

    def open_restaurant(self):
        print("Restaurant is opening right now")

    def read_served_clients(self) -> object:
        print("Number of served clients is  " + str(self.number_served) + " !" )

    def update_served_client(self, clients):
        if clients >= self.number_served:
            self.number_served = clients
        else:
            print("You can not decrease number of served client")
    def increment_number_served(self, client):
        self.number_served += client




restaurant = Restaurant("Inna's pizza", 'italiano')
print(restaurant.describe_restaurant())
restaurant.update_served_client(15)
restaurant.read_served_clients()
restaurant.increment_number_served(3)
restaurant.read_served_clients()