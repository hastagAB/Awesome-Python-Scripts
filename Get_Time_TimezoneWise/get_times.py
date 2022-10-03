# First Install Using The Command Below:
# pip install pytz

from datetime import datetime
import pytz

# list of desired countries
Country_Zones = pytz.all_timezones  # pytz.all_timezones will create a list with name of all timezones

country_time_zones = []

for country_time_zone in Country_Zones:
    country_time_zones.append(pytz.timezone(country_time_zone))

for i in range(len(country_time_zones)):
    country_time = datetime.now(country_time_zones[i])
    print(f"The date of {Country_Zones[i]} is {country_time.strftime('%d-%m-%y')} and The time of {Country_Zones[i]} is {country_time.strftime('%H:%M:%S')}") #prints current time of all timezones in Country_Zones
    
