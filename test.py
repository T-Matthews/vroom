import requests



included_makes = ['toyota','honda','chevrolet','ford','mercedes_benz','jeep',
                    'bmw','porsche','subaru','nissan','cadillac','volkswagen',
                    'lexus','audi','ferrari','volvo','jaguar','gmc','buick',
                    'acura','bentley','dodge','hyundai','lincoln','mazda',
                    'land rover', 'tesla','ram_trucks','kia','chrysler',
                    'pontiac','infiniti','mitsubishi','oldsmobile','maserati',
                    'aston_martin','bugatti','fiat','mini','alfa_romeo','saab']
for x in included_makes:
    
    api_url = 'https://api.api-ninjas.com/v1/cars?make='+x
    print(api_url)