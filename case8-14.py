def car_profile(manufacturer,model_name,**other_details):
    profile = {}
    profile['manufacturer_company'] = manufacturer
    profile['model'] = model_name
    for key, value in other_details.items():
        profile[key] = value
    return profile
car = car_profile(
    'subaru','outback',
    color='red',
    tow_package = True ,
    parktronic = True
    )
print(car)