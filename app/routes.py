from app import app
import requests
import os


from flask import render_template

@app.route('/')
def home():
    greeting = "Hello"
    return render_template('index.html',g=greeting)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cars')
def update():
    api_key = os.environ.get('API_KEY')
    api_url = 'https://api.api-ninjas.com/v1/cars'
    car_data = {}
    included_makes = ['toyota','honda','chevrolet','ford','mercedes_benz','jeep',
                    'bmw','porsche','subaru','nissan','cadillac','volkswagen',
                    'lexus','audi','ferrari','volvo','jaguar','gmc','buick',
                    'acura','bentley','dodge','hyundai','lincoln','mazda',
                    'land rover', 'tesla','ram_trucks','kia','chrysler',
                    'pontiac','infiniti','mitsubishi','oldsmobile','maserati',
                    'aston_martin','bugatti','fiat','mini','alfa_romeo','saab']
    for x in included_makes:
        api_url = 'https://api.api-ninjas.com/v1/cars?make='+x

        new_data = requests.get(api_url, headers={'X-Api-Key': api_key})
        if new_data.status_code==requests.codes.ok:
            #add exception for RAM Trucks
            if x == 'ram_trucks':  
                car_data['dodge'] = new_data.json()
            else:
                car_data[x]=new_data.json()
        else:
            print("issue with "+x)
    print(car_data)
    return render_template('cars.html',car_data=car_data)
    



  



   
    # if response.status_code == requests.codes.ok:
    #     print(response)
    # else:
    #     print("Error:", response.status_code, response.text)