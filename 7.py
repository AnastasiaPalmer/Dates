"""
Створіть функцію, яка буде зчитувати дані з одного типу файлу та зберігати їх у файлі іншого типу.

Вона буде приймати 3 аргументи:
- шлях до файлу;
- змінну, яка буде визначати тип цього файлу;
- змінну, яка буде визначати тип файлу, у який потрібно зберегти дані.

Функція буде працювати з файлами типу *.txt, *.csv, *.dat. Протестуйте роботу функції…
"""

import csv
import pickle

def Convertor(FileName, TypeIn, TypeOut):
    if   TypeIn == 'csv' and TypeOut == 'txt':
        fdi = open(FileName + '.' + TypeIn, "r")        # File descriptor INPUT
        fdo = open(FileName + '.' + TypeOut, "w")       # File descriptor OUTPUT
        csvreader = csv.reader(fdi)
        for row in csvreader:
            sep=""; line=""
            for field in row:
                line = line + sep + field
                sep = ' '
            fdo.write(line+'\n')
        fdi.close()
        fdo.close()

    elif TypeIn == 'csv' and TypeOut == 'dat':
        fdi = open(FileName + '.' + TypeIn , "r")       # File descriptor INPUT
        csvreader = csv.reader(fdi)
        data = []
        for row in csvreader:
            data.append(row)
        file = open(FileName + '.' + TypeOut, "wb")    # File descriptor OUTPUT
        pickle.dump(data, file)
        fdi.close()

    elif TypeIn == 'dat' and TypeOut == 'csv':
        fdi = open(FileName + '.' + TypeIn, "rb")    # File descriptor INPUT
        data = pickle.load(fdi)
        fdi.close()
        print('Data:', data)

        file = open(FileName + '1.' + TypeOut, "w", newline="")  # File descriptor OUTPUT
        writer = csv.writer(file)
        writer.writerows(data)

    elif TypeIn == 'dat' and TypeOut == 'txt':
        fdi = open(FileName + '.' + TypeIn, "rb")    # File descriptor INPUT
        data = pickle.load(fdi)
        fdi.close()
        fdo = open(FileName + '1.' + TypeOut, "w")  # File descriptor OUTPUT
        for row in data:
            sep=""; line=""
            for field in row:
                line = line + sep + field
                sep = ' '
            fdo.write(line+'\n')

    elif TypeIn == 'txt' and TypeOut == 'csv':
        file = open(FileName + '.' + TypeIn, "r")    # File descriptor INPUT
        data = file.readlines()
        file.close()
        print(data)

        temp = []
        for line in data:
            line = line.strip()
            fields = line.split(' ')
            temp.append(fields)
        print(temp)

        data = temp

        file = open(FileName + '2.' + TypeOut, "w", newline="")  # File descriptor OUTPUT
        writer = csv.writer(file)
        writer.writerows(data)

    elif TypeIn == 'txt' and TypeOut == 'dat':
        file = open(FileName + '.' + TypeIn, "r")    # File descriptor INPUT
        data = file.readlines()
        file.close()
        print(data)

        temp = []
        for line in data:
            line = line.strip()
            fields = line.split(' ')
            temp.append(fields)
        print(temp)

        data = temp

        file = open(FileName + '2.' + TypeOut, "wb")  # File descriptor OUTPUT
        pickle.dump(data, file)
        file.close()

#Convertor('cotleta', 'csv', 'txt')
#Convertor('cotleta', 'csv', 'dat')
#Convertor('cotleta', 'dat', 'csv')
#Convertor('cotleta', 'dat', 'txt')
#Convertor('cotleta', 'txt', 'csv')
Convertor('cotleta', 'txt', 'dat')

# if      in=txt : read txt => data
# else if in=csv : read csv => data
# else if in=dat : read dat => data
# data = convert(in,out,data)
# if      ou=txt : writeTxt(data)
# else if ou=csv : writeCsv(data)
# else if ou=dat : writeDat(data)
