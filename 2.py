"""
 Продемонструйте роботу зазначених методів бібліотеки os.
 Дізнайтесь, будь-ласка, як тут можуть використовуватись т.з. «сирі» текстові змінні («сырые строки»).
               "Сырые" строки - подавляют экранирование.
"""
# import os
#
# os.mkdir("Buba")                   # створює нову папку
#
# if os.path.exists("Buba"):         # повертає True/False, якщо файл існує
#     print("File exist")
# else:
#     print("File does not exist")
#
# os.rename("Buba", "Boba")          # перейменовує директорію
# os.chdir('Boba')
# f = open("Pupa.txt", "a")  # ????
# f.close()
#
# os.chdir('..')
# os.remove("Pupa.txt")              # видаляє файл
#
# os.rmdir("Boba")                   # видаляє папку
#
#
#
#
"""
Продемонструйте роботу зазначених методів бібліотеки os.
"""
import os

if os.path.exists("Buba"):
    os.rmdir('Buba')
if os.path.exists("Boba/Pupa.txt"):
    os.unlink('Boba/Pupa.txt')
if os.path.exists("Boba"):
    os.removedirs('Boba')

#os.rmdir('Boba')
#os.system("del Boba")

os.mkdir("Buba")                   # створює нову папку
if os.path.exists("Buba"):         # повертає True/False, якщо файл існує
    print("Dir exist")
else:
    print("Path does not exist")
    exit(1)

os.rename("Buba", "Boba")          # перейменовує директорію
f = open("Boba/Pupa.txt", "a")
f.close()

stat = os.stat('Boba/Pupa.txt')
# print('Object is:',  stat.st_mode, 'size:', stat.st_size, 'time:', datetime(stat.st_mtime).strftime('%F,%T'), os.path.isdir())
print('Object is:',  stat.st_mode, 'size:', stat.st_size, 'isdir:', os.path.isdir('Boba/Pupa.txt'))


os.remove(  "Boba/Pupa.txt")              # видаляє файл
os.remove("/Boba/Pupa.txt")              # видаляє файл

os.rmdir("Boba")                    # видаляє папку
cur = os.getcwd()                   # Ой, мамо! Де я ?!  current working directory

print('Ok! We are at end! Congratulation! :-) We are in [', cur, ']')
