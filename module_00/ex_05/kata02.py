# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

import datetime
date = datetime.datetime(*kata)
#the methode datetime() convert elements of the tuple to: 2019-09-25 03:30:00 
#the methode strftime convert datetime object to a specific string format 
#the desired string format: month/day/year hour:minute
print(date.strftime("%m/%d/%Y %H:%M"))