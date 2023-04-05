from app import app
import requests
import os
from app.services import CarForm,initial,get_gas_price



from flask import render_template,request



@app.route('/',methods = ['POST', 'GET'])
def home():
    for x in initial:
         x=None
    form=CarForm()
    if form.validate_on_submit():
        print('VALID')
        zip_code=int(form.zip_code.data)
        gas_price=get_gas_price(zip_code)
        print(gas_price,"HERE")
        input_data={
                        'make' : form.make.data,
                        'model' : form.model.data,
                        'msrp' : form.msrp.data,
                        'fuel_type':form.fuel_type.data,
                        'mpg' : form.mpg.data,
                        'annual_milage':form.annual_milage.data,
                        'zip_code':form.zip_code.data,
                        'gas_price':gas_price
                    }
        for k,v in input_data.items():
            print(k,v)
    else:
        print('FAILED')      
        return render_template('index.html',form=form)
    return render_template('index.html',input_data=input_data,form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cars',methods = ['POST', 'GET'])
def cars():
       return render_template('cars.html')


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