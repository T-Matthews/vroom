from app import app
import requests
import os


from flask import render_template,request

@app.route('/',methods = ['POST', 'GET'])
def home():
    form_data = request.form
    return render_template('index.html',form_data=form_data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cars',methods = ['POST', 'GET'])
def cars():
    if request.method == "POST":
       # getting input with name = fname in HTML form
        name = request.form.get("name")
       
        city = request.form.get("City")
        country = request.form.get('Country')
        print(type(name), type(city), type(country))
        form_data = request.form
        return render_template('cars.html',form_data=form_data)

    return render_template('index.html')


    # api_key = os.environ.get('API_KEY')
    # api_url = 'https://api.api-ninjas.com/v1/cars'
    # car_data = {}
    # included_makes = ['toyota','honda','chevrolet','ford','mercedes_benz','jeep',
    #                 'bmw','porsche','subaru','nissan','cadillac','volkswagen',
    #                 'lexus','audi','ferrari','volvo','jaguar','gmc','buick',
    #                 'acura','bentley','dodge','hyundai','lincoln','mazda',
    #                 'land rover', 'tesla','ram_trucks','kia','chrysler',
    #                 'pontiac','infiniti','mitsubishi','oldsmobile','maserati',
    #                 'aston_martin','bugatti','fiat','mini','alfa_romeo','saab']
    # for x in included_makes:
    #     api_url = 'https://api.api-ninjas.com/v1/cars?make='+x

    #     new_data = requests.get(api_url, headers={'X-Api-Key': api_key})
    #     if new_data.status_code==requests.codes.ok:
    #         #add exception for RAM Trucks
    #         if x == 'ram_trucks':  
    #             car_data['dodge'] = new_data.json()
    #         else:
    #             car_data[x]=new_data.json()
    #     else:
    #         print("issue with "+x)
    # print(car_data)
    # return render_template('cars.html',car_data=car_data)
    



  



   
    # if response.status_code == requests.codes.ok:
    #     print(response)
    # else:
    #     print("Error:", response.status_code, response.text)