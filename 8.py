"""
Використовуючи засоби Python та наш датасет, дайте відповідь на наступні питання:
 1. Яка загальна кількість хворих зафіксовано на Філіппінах на 30.08.2020?
 2. Коли був зафіксований найбільший приріст хворих за тиждень в Україні?
 3. Порахуйте, чи відповідають дані по загальній кількості випадків за 21.08.2020 по світу сумі випадків по країнах за цю дату?
 4. Запишіть в текстовий файл найбільший показник по випадкам по кожній з країн. Н-д: Ukraine =)
"""

from datetime import date
import csv

# кількість хворих зафіксовано на Філіппінах на 30.08.2020

fd = open("owid-covid-data.csv", "r")
csvreader = csv.reader(fd)
for row in csvreader:
    if row[2] == 'Philippines' and (row[3] == '30.08.2020' or row[3] == '2020-08-30'):
        print(row[2], row[3], "; Кількість хворих зафіксовано: ", row[4])
fd.close()


fd = open("owid-covid-data.csv", "r")
csvreader = csv.reader(fd)
data = []
for row in csvreader:
    data.append(row)
fd.close()

before30 = '1900-01-01'
for row in data:
    if row[2] == 'Philippines' and row[3] < '2020-08-30':
        if row[3]>before30:
            before30 = row[3]
for row in data:
    if row[2] == 'Philippines' and row[3]==before30:   # (row[3] == '30.08.2020' or row[3] == '2020-08-30'):
        print(row[2], row[3], "; 2Кількість хворих зафіксовано: ", row[4])


# Коли був зафіксований найбільший приріст хворих за тиждень в Україні?


def week_number(dt):  # Expecting: '2020-08-30'
    d = dt.split('-')
    year = int(d[0])
    month = int(d[1])
    day = int(d[2])
    # print('date conversion:', dt, 'Array:', d, 'DATE:', date(year,month,day) , date(year,month,day).strftime('%Y_%W'))
    return date(year, month, day).strftime('%Y_%W')


weekly = {}
for row in data:
    if row[2] == 'Ukraine':
        yw = week_number(row[3])
        cases = float(row[4])
        if yw in weekly.keys():
            weekly[yw] = weekly[yw] + cases
        else:
            weekly[yw] = cases
# print(weekly)

maxv = 0
week = '?'
for key, value in weekly.items():
    # print(key,'=',value)
    if value > maxv:
        maxv = value
        week = key
print("Max cases week is", week)
print("Cases: ", maxv)

# Порахуйте, чи відповідають дані по загальній кількості випадків за 21.08.2020 по світу
# сумі випадків по країнах за цю дату?
World = 0
Country = 0
for row in data:
    if row[3] == "2020-08-21":
        try:
            cases = float(row[4])
        except:
            cases = 0
        if row[2] == "World":
            World = World + cases
        else:
            Country = Country + cases
print("  World cases for 2020-08-21:", World)
print("Country cases for 2020-08-21:", Country)


# найбільший показник по випадкам по кожній з країн. Н-д: Ukraine = 0

max_value = {}
for row in data:
    if row[2] != 'World' and row[2] != 'location':
        try:
            cases = float(row[4])
        except:
            cases = 0
        country = row[2]
        if country in max_value.keys():
            max_value[country] = max_value[country] + cases
        else:
            max_value[country] = cases
for key, value in max_value.items():
    print(key, '=', value)


