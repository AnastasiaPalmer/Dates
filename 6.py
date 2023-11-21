from datetime import datetime
"""
Виведіть поточну дату у форматах, прийнятих у різних сторdнах світу.
"""

date = datetime(1970, 1, 1)

print("              Ukraine: ", date.strftime('%d.%m.%Y'))  # DD-MM-YYYY
print("               Poland: ", date.strftime('%Y.%m.%d'))  # YYYY-MM-DD
print("                  USA: ", date.strftime('%m.%d.%Y'))  # MM-DD-YYYY
print("International English: ", date.strftime('%d.%m.%Y'))  # DD-MM-YYYY
print("        Great Britain: ", date.strftime('%d.%m.%Y'))  # DD/MM/YYYY
print("               Sweden: ", date.strftime('%Y.%m.%d'))  # YYYY-MM-DD

