# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.
import datetime
import pytz

# 0: Quit
zones = {'1': 'Africa/Addis_Ababa',
         '2': 'America/Argentina/Buenos_Aires',
         '3': 'America/Barbados',
         '4': 'America/La_Paz',
         '5': 'Antarctica/Troll',
         '6': 'Asia/Bangkok',
         '7': 'Asia/Beirut',
         '8': 'Asia/Jakarta',
         '9': 'Asia/Phnom_Penh',
         }

print('Please Select Time Zone:')
print('*' * 40)
print('0: For Exit')
for number, name in zones.items():
    print(f'{number} : {name}')

choice = None
while True:
    choice = input()

    if choice == '0':
        break

    if choice in zones.keys():
        n_zone = pytz.timezone(zones[choice])
        time_in_n = datetime.datetime.now(tz=n_zone)
        local_time = datetime.datetime.now()
        utc_time = datetime.datetime.utcnow()
        print(f'You selected:\t\t\t {choice} : {n_zone}\n'
              f'current date and time:\t {time_in_n}\n'
              f'Your local time is:\t\t {local_time}\n'
              f'and UTC time is:\t\t {utc_time}')

