from app import app
from app.services import CarForm,get_prices



from flask import render_template,jsonify,request



@app.route('/',methods = ['POST', 'GET'])
def home():
    form=CarForm()
    if form.validate_on_submit():
        print('VALID')
        zip_code=int(form.zip_code.data)
        ele_price,gas_price=get_prices(zip_code)
        print(gas_price,"HERE")
        input_data={
                        'make' : form.make.data,
                        'model' : form.model.data,
                        'msrp' : form.msrp.data,
                        'fuel_type':form.fuel_type.data,
                        'mpg' : form.mpg.data,
                        'annual_milage':form.annual_milage.data,
                        'zip_code':form.zip_code.data,
                        'gas_price':gas_price,
                        'ele_price':ele_price
                    }
        for k,v in input_data.items():
            print(k,v)
    else:
        print('FAILED')      
        return render_template('index.html',form=form)
    return render_template('index.html',input_data=input_data,form=form)


@app.route(f'/fuel_price',methods = ['POST', 'GET'])
def fuel_price():
       zip_code=request.args.get('zip')
       ele_price,gas_price=get_prices(zip_code)
       return jsonify({'electricity':{'cost':ele_price,
                                      'units':'cents/kWhr'},
                        'gasoline':{'price':gas_price,
                                    'units':'dollars/gallon'}})


    



  



   
    # if response.status_code == requests.codes.ok:
    #     print(response)
    # else:
    #     print("Error:", response.status_code, response.text)