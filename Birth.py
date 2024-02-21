from datetime import datetime
YouAge=input("Enter Your Birthdate YYYY-MM-DD: ")
birthdate=datetime.strptime(YouAge,'%Y-%m-%d')
today=datetime.today()
age=today.year-birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.day))
# age=today.year-birthdate.year-(today.month-birthdate.month)-(today.day-birthdate.day)
print("Your age is:",age)