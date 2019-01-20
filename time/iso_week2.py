import datetime

from datetime import date

month = datetime.datetime.now().strftime("%m")
weekNumber = date.today().isocalendar()[1]
print('Week number:', weekNumber, "Month number:",month)






