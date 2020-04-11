class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name.title() + " !")
        print("Type of cuisine is " + self.cuisine_type.title() + " .")

    def open_restaurant(self):
        print("Restaurant is opening right now")

restaurant = Restaurant('europe', 'mediteranian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
