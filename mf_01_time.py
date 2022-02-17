import time

# print(time.gmtime(0))
#
# print(time.localtime(time.time()))
#
# print(time.time())

# Date:
# time_here = time.localtime()
# print(time_here)
# print('Year: ', time_here[0], time_here.tm_year)    # two ways to, code is equal - no practical diff
# print('Month: ', time_here[1], time_here.tm_mon)    # second way is easier to read
# print('Day: ', time_here[2], time_here.tm_mday)

# from time import time as my_timer         # cheat on pressing double ENTER
from time import perf_counter as my_timer
import random

input('Press ENTER to start')


wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input('Press ENTER to stop')
end_time = my_timer()

print('Started at: ' + time.strftime("%X", time.localtime(start_time)))
print('Stopped at: ' + time.strftime("%X", time.localtime(end_time)))
print(f'Your reaction time was {end_time - start_time} seconds')