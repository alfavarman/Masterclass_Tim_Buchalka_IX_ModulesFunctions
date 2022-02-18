import pytz
import datetime

country = 'Europe/Moscow'
to_displ = pytz.timezone(country)
loc_time = datetime.datetime.now(tz=to_displ)
print(loc_time)
print(country)
print(datetime.datetime.utcnow())

for x in pytz.all_timezones:             # timezones
    print(x)

for x in pytz.country_names:             # iso316 country codes
    print(x + ": " + pytz.country_names[x])
