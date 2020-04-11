class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nThe restaurant name is " + self.restaurant_name.title() + " !")
        print("Type of cuisine is " + self.cuisine_type.title() + " .")

    def open_restaurant(self):
        print("Restaurant is opening right now")

restaurant = Restaurant('up_town','european')
restaurant_1 = Restaurant("anddy's pizza", "italian")
restaurant_2 = Restaurant('dublin', 'pub')
restaurant.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
