fuel_type_list = ['Regular Gasoline', 'Mid-Grade Gasoline','Premium Gasoline','---------------------','Diesel','---------------------','EV']
from flask_wtf import FlaskForm
from statistics import mean
from wtforms import StringField, SubmitField,IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange
from uszipcode import SearchEngine
import os,requests,datetime



#Create the CarForm WTForms Template
class ZipForm(FlaskForm):
    zipcode = IntegerField("Zipcode",validators = [DataRequired()])
   


def get_prices(zipcode):
    search=SearchEngine()
    # get lat long, state abbr from zip code
    lat=search.by_zipcode(zipcode).lat
    long=search.by_zipcode(zipcode).lng
    state_abbr=search.by_zipcode(zipcode).state_abbr
    # make call to gasbuddy for regional average gas cost
    api_url = f"https://www.gasbuddy.com/gaspricemap/county?lat={lat}&lng={long}&usa=true"
    response = requests.post(api_url)
    gas_price= response.json()[0]['Price']
    
    #make call to EIA to get residential Electrical data
    EIA_KEY=os.environ.get('EIA_KEY')
    #Gathering historical data. Need to specify start date for collection
    today = datetime.date.today()
    #Specify umber of years of data collected
    years_history = 2
    #Gets date of start of data collection
    history_start=str(today-datetime.timedelta(days=(365*years_history)))
    

    #API call returns all electricity rates since {years_history}. 
    ele_API_url=f'https://api.eia.gov/v2/electricity/retail-sales/data?api_key={EIA_KEY}&data[]=price&facets[stateid][]={state_abbr}&facets[sectorid][]=RES&start={history_start}'
    response=requests.get(ele_API_url).json()['response']['data']
    most_recent=0
    ele_price=0
    for x in response:
        #Turns date into a decimal, for easy numerical comparison
        date=float(str(x['period'][:4])+'.'+str(x['period'][5:]))
        #If a date is more recent than the previous, then it will reset the price and update the most recent date
        if date>most_recent:
            ele_price=x['price']
            most_recent=date
    return ele_price,gas_price

    
