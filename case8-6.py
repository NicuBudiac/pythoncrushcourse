def city_country(city_name,country_name):
    city_format = '"' + city_name + ", " + country_name + '"'
    return city_format.title()
city = city_country('santiago','chile')
city1 = city_country('new york','usa')
city2 = city_country('paris','france')
l = [city,city1,city2]
for n in l:
    print(n)