holidays = {
    "January 1": "New Year's Day",
    "July 1": "Canada Day",
    "December 25": "Christmas Day"}


month = input("Enter the month: ")
day = int(input("Enter the day: "))

month_str = str(month)
day_str = str(day)

date_str = month_str + " " + day_str

if date_str in holidays:
    print(holidays[date_str])
else:
    print("The entered month and day do not correspond to a fixed-date holiday.")
