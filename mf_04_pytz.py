import pytz
import datetime

# country = 'Europe/Moscow'
# to_displ = pytz.timezone(country)
# loc_time = datetime.datetime.now(tz=to_displ)
# print(loc_time)
# print(country)
# print(datetime.datetime.utcnow())
#
# for x in pytz.all_timezones:             # timezones
#     print(x)
#
# for x in pytz.country_names:             # iso316 country codes
#     print(x + ": " + pytz.country_names[x])
#
# for x in pytz.country_names:             # country code: country name : country time zone
#     # print(f'{x} : {pytz.country_names[x]} : {pytz.country_timezones.[x]}') # crashes because no timezone for Buvut Island
#     print(f'{x} : {pytz.country_names[x]} : {pytz.country_timezones.get(x)}')

# for x in pytz.country_names:
#     if x in pytz.country_timezones:
#         for zone in sorted(pytz.country_timezones[x]):
#             time_display = pytz.timezone(zone)
#             local_time = datetime.datetime.now(tz=time_display)
#             print(f'{zone} \t\t {local_time}')
#     else:
#         pass


local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()
print(f'local_time = datetime.datetime.now(): {local_time}')
print(f'utc_time = datetime.datetime.utcnow(): {utc_time}')

aware_local_time = pytz.utc.localize(local_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print(f'aware_local_time = pytz.utc.localize(local_time).astimezone(): {aware_local_time}, {aware_local_time.tzinfo}')
print(f'aware_utc_time = pytz.utc.localize(utc_time) {aware_utc_time}, {aware_utc_time.tzinfo}')

gap_time = datetime.datetime(2022, 2, 18, 16, 41, 0, 0)
print(gap_time)
print(gap_time.timestamp())

s = gap_time.timestamp()
t = s + (60 * 60)

# print(pytz.all_timezones)
# print('Asia/Bangkok' in pytz.all_timezones)
th = pytz.timezone('Asia/Bangkok')                                                        # doesnt work with TH
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(th)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(th)

print(f'{s} since start of epoch CODE: (dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(th)) '
      f'{dt1}')
print(f'{t} since start of epoch CODE: (dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(th)) '
      f'{dt2}')