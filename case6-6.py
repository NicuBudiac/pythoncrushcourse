favorite_language = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil' : 'python',
    }
friends = ['phil','sarah','nicu','inna']
for name in friends:
    if name in favorite_language.keys():
        print(name.title() + ", you alredy taked the poll !!!")
    else:
        print(name.title() + " , you should take the poll !!!")