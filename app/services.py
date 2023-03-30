fuel_type_list = ['Regular Gasoline', 'Mid-Grade Gasoline','Premium Gasoline','---------------------','Diesel','---------------------','EV']
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange
from uszipcode import SearchEngine
import os
search=SearchEngine()
#Create the CarForm WTForms Template
class CarForm(FlaskForm):
    make = StringField("Vehicle Make")
    model = StringField("Vehicle Model")
    msrp = IntegerField('MSRP',validators=[DataRequired()])
    fuel_type = SelectField('Fuel Type',choices=fuel_type_list,validators=[DataRequired()])
    mpg = IntegerField("Vehicle MPG",validators = [DataRequired()])
    annual_milage=IntegerField("Annual Milage",validators = [DataRequired()])
    zip_code = IntegerField("Annual Milage",validators = [DataRequired(),NumberRange(min=10000,max=99999,message="Invalid 5 digit Zip")])
    submit = SubmitField()

initial = ['make','model','mpg','msrp','fuel_type','annual_milage','zip_code']


#Get City, State from Zip Code

search=SearchEngine()
def zip_to_city(x):
    search=SearchEngine()
    city = search.by_zipcode(x).major_city
    state=search.by_zipcode(x).state_abbr
    if city and state:
        return city,state
    elif state:
        return state
    else:
        return 'None'

#Get Fuel Price for City. If City not in DB, state used instead
def getprices(x):
    city,state=zip_to_city(x)
    print(city,state)
    import http.client
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': #GAS KEY HERE
        }

    conn.request("GET", f"/gasPrice/stateUsaPrice?state={state}", headers=headers)

    res = conn.getresponse()

    str_data = res.read().decode('utf-8')

    success=False
    if city in str_data:
        str_data=str_data[34:str_data.index(city)]
        diesel = float(str_data[-15:-10])
        premium=float(str_data[-32:-27])
        midgrade=float(str_data[-50:-45])
        gasoline=float(str_data[-69:-64])
        success=True
    else:

        str_data=str_data[:str_data.index('}')]

        diesel = float(str_data[-8:-3])
        premium=float(str_data[-25:-20])
        midgrade=float(str_data[-43:-38])
        gasoline=float(str_data[-62:-57])

    print(diesel)
    print(premium)
    print(midgrade,type(midgrade))
    print(gasoline,type(gasoline))
    return(success,gasoline,midgrade,premium,diesel)
getprices(91962)


# print(zco(80129))

