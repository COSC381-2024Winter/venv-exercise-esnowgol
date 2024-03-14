from random_strings import random_string
import metric_time #requires pytz
import BigChars as banner



characters="~-_*#@+="
myRandChars = random_string(45,character_string=random_string(2,character_string=characters))
republicanCal = metric_time.RepublicanCalendar()
banner.big_print("Calendar", 2, '%')
print(str(republicanCal.now()))
print(myRandChars)

