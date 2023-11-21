from datetime import datetime
"""
Розрахуйте дату свого народження та свій вік (від сьогодні)
так, як його рахує комп’ютер (у мілісекундах). Використайте відповідні бібліотеки.
"""

birthdate = datetime(2004, 6, 13, 11, 32, 24, 847)
#print(birthdate)
#print(birthdate.strftime('%d.%m.%Y %H:%M:%S'))

datenow = datetime.now()
#print(datenow.strftime('%d.%m.%Y %H:%M:%S'))

age = datenow - birthdate
print('Total age   ', age)
print('Days/Seconds/Microseconds ', age.days, age.seconds, age.microseconds)
print('in millisec', age.days * 24*60*60*1000 + age.seconds * 1000 + age.microseconds / 1000)
print('in millisec', age.total_seconds()*1000)


#print('10 hours in sec = 10*60*60', 10*60*60)
#print('Seconds', age.seconds, 'H', age.seconds/60/60, 'M', age.seconds/60)
