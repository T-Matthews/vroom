from app import app
from app.services import ZipForm,get_prices



from flask import render_template,jsonify,request,redirect,url_for


@app.route(f'/fuel_price/<int:zipcode>',methods = ['POST', 'GET'])
def fuel_price(zipcode):
       
       ele_price,gas_price=get_prices(zipcode)
       return jsonify({'electricity':{'cost':ele_price,
                                      'units':'cents/kWhr'},
                        'gasoline':{'price':gas_price,
                                    'units':'dollars/gallon'}})

@app.route('/',methods = ['POST', 'GET'])
def home():
    curr_price=None
    zipcode=None
    form=ZipForm()
    if form.validate_on_submit():
        print('VALID')
        zipcode=int(form.zipcode.data)
        ele_price,gas_price=get_prices(zipcode)
        curr_price={
             'electric':ele_price,
             'gasoline':gas_price
        }
        print(zipcode," : ZIP")
    else:
        print('FAILED')      
    return render_template('index.html',form=form,price=curr_price)





    



  



   
    # if response.status_code == requests.codes.ok:
    #     print(response)
    # else:
    #     print("Error:", response.status_code, response.text)