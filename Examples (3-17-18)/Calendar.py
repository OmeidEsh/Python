#Calendar

import calendar

print(calendar.month(2018,3))
print("is 2018 a leap year?", calendar.isleap(2018))
print("Number of leapdays 1990-2018: ", calendar.leapdays(1990,2018))
print("Set sunday as first week day.")
calendar.setfirstweekday(6)
print(calendar.month(2018,3))
print("week day for 13 March 2018 is: ", calendar.weekday(2018,3,13))