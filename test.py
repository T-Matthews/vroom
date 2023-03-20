import requests




api_url = 'https://api.api-ninjas.com/v1/cars'
car_data = {}
included_makes = ['toyota']
"""

,'honda','chevrolet','ford','mercedes_benz','jeep',
                'bmw','porsche','subaru','nissan','cadillac','volkswagen',
                'lexus','audi','ferrari','volvo','jaguar','gmc','buick',
                'acura','bentley','dodge','hyundai','lincoln','mazda',
                'land rover', 'tesla','ram_trucks','kia','chrysler',
                'pontiac','infiniti','mitsubishi','oldsmobile','maserati',
                'aston_martin','bugatti','fiat','mini','alfa_romeo','saab']
"""
# for x in included_makes:
#     api_url = 'https://api.api-ninjas.com/v1/cars?make='+x
#     new_data = requests.get(api_url, headers={'X-Api-Key': 'ilgqmSKRzBK90jvnTHceOg==vMoGd0XzjwCjSfDI'})
#     if new_data.status_code==requests.codes.ok:
#         #add exception for RAM Trucks
#         if x == 'ram_trucks':  
#             car_data['dodge'] = new_data.json()
#         else:
#             car_data[x]=new_data.json()
#     else:
#         print("issue with "+x)
# print(car_data)

#same as car Data
car_data1={'toyota': [{'city_mpg': 23, 'class': 'compact car', 'combination_mpg': 24, 'cylinders': 4, 'displacement': 1.6, 'drive': 'fwd', 'fuel_type': 'gas', 'highway_mpg': 26, 'make': 'toyota', 'model': 'corolla', 'transmission': 'a', 'year': 1993}, {'city_mpg': 23, 'class': 'compact car', 'combination_mpg': 26, 'cylinders': 4, 'displacement': 1.6, 'drive': 'fwd', 'fuel_type': 'gas', 'highway_mpg': 31, 'make': 'toyota', 'model': 'corolla', 'transmission': 'm', 'year': 1993}, {'city_mpg': 23, 'class': 'compact car', 'combination_mpg': 25, 'cylinders': 4, 'displacement': 1.8, 'drive': 'fwd', 'fuel_type': 'gas', 'highway_mpg': 30, 'make': 'toyota', 'model': 'corolla', 'transmission': 'a', 'year': 1993}, {'city_mpg': 23, 'class': 'compact car', 'combination_mpg': 26, 'cylinders': 4, 'displacement': 1.8, 'drive': 'fwd', 'fuel_type': 'gas', 'highway_mpg': 30, 'make': 'toyota', 'model': 'corolla', 'transmission': 'm', 'year': 1993}, {'city_mpg': 18, 'class': 'midsize car', 'combination_mpg': 21, 'cylinders': 4, 'displacement': 2.2, 'drive': 'fwd', 'fuel_type': 'gas', 'highway_mpg': 26, 'make': 'toyota', 'model': 'camry', 'transmission': 'a', 'year': 1993}]}

my_cars = {}
for k,v in car_data1.items():
    my_cars[k] = {}
    for x in v:
        print(x)

  
        
            #           = { 
            # 'fuel_type': x['fuel_type'],
            # 'city_mpg':x['city_mpg'],
            # 'hwy_mpg':x['hwy_mpg'],
            # 'mpg': x['combination_mpg']
print(my_cars)
    #     } 
    #                 }

