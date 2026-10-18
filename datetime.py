from datetime import date,datetime

today = date.today()
now = datetime.now()

print("Current Date:",today)
print("Current Year:",today.year)
print("Current Month:",today.month)
print("Current Day:",today.day)
print("Current Hour:",now.hour)