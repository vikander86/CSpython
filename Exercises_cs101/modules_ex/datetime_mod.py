from datetime import datetime

datetime.now()

subtracting_dates = datetime.now() - datetime(2018, 1, 1)
print(subtracting_dates)

#parse a date
parsed_date = datetime.strptime('Jan 15, 2018','%b %d, %Y')
print(parsed_date.month)
print(parsed_date.year)
print(parsed_date.day)

#converts a date to a string
date_string = datetime.strftime(datetime.now(),'%b %d, %Y')
print(date_string)