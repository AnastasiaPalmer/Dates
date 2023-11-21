import re
from datetime import date
"""
Створіть функцію, яка має наступний функціонал: користувач вводить дату да текст.
Функція записує у файл «Календар» дату та відповідну подію. Сортувати дати не потрібно.
"""

class Event:
    def __init__(self):
        self.date  = 'yyyy-mm-dd'
        self.event = 'event'
        self.text  = 'yyyy-mm-dd event'



def check_date(s, newRec):
    dt = s[0:10]
    dt = dt.replace("/", "-").replace(' ', '-').replace(',', '-').replace('.', '-')
    # we have: expecting: yyyy-mm-dd
    kus = dt.split('-')

    try:
        new_date = date(int(kus[0]), int(kus[1]), int(kus[2])) # Year, Month, Day
    except:
        print('Hmmm :-( Wrong date: ' + dt)
        return False

    print('Date for new event is: ' + new_date.strftime('<%Y-%m-%d>') )
    if new_date:
        newRec.date = new_date.strftime('%Y-%m-%d')
        newRec.event = s[11:]
        newRec.text = newRec.date + ' ' + newRec.event
        return True
    else:
        print("Wrong date:"+dt)
        return False


def check(s, newRec):
    regex = re.compile('[0-9]{4}[-/ .,][0-9]{2}[-/ .,][0-9]{2}[ \t].+')
    if re.fullmatch(regex, s):
        print("Entered date event")
        if check_date(s, newRec):
            pass
        else:
            # print("ERROR!!! Seems, it is not date:"+s[0:10])
            return False
        return True
    else:
        print("-_-")
        return False


newRec = Event()

s = input("Enter date event: ")
if check(s, newRec):
    f = open("calendar.txt", "a")
    f.write(newRec.text+"\n")
    f.close()
else:
    print("I can not add wrong event message into calendar!")
    exit(1)

