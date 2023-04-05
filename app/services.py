fuel_type_list = ['Regular Gasoline', 'Mid-Grade Gasoline','Premium Gasoline','---------------------','Diesel','---------------------','EV']
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange
from uszipcode import SearchEngine
import os,requests
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


def get_gas_price(x):
    search=SearchEngine()
    lat=search.by_zipcode(x).lat
    long=search.by_zipcode(x).lng
    api_url = f"https://www.gasbuddy.com/gaspricemap/county?lat={lat}&lng={long}&usa=true"
    response = requests.post(api_url)
    gas_price= response.json()[0]['Price']
    return gas_price




