cities = "\nPlease enter the name of the city you visited"
cities += "\nEnter 'quit' when you are finished"
active = True
while active:
    city = input(cities)

    if city == 'quit':
        break
    else:
        print("\n" + city.title() + "it's a beutiful city")