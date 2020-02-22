my_animals = ['dog', 'cat', 'mouse']
friend_animal = my_animals[:]
my_animals.append('frog')
friend_animal.append('monkey')
print("My favorite animal are :")
for animal in my_animals:
    print(animal)
print("My friend favorite animal are :")
for animal1 in friend_animal:
    print(animal1)
