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

class IceCream(Restaurant):
    def __init__(self,restaurant_name, cuisine_type):
        super().__init__ (restaurant_name , cuisine_type )
        self.flavors = ['air_spencer','oziuam_spoke','little_tres','chemikal_guys','meso_natural']

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)

IceCreamStand = IceCream('IceCream','american')
IceCreamStand.display_flavors()
IceCreamStand.describe_restaurant()