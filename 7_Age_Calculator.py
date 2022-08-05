#import datetime as datetime
from datetime import *
a=78
print("Enter Your Birthday")
year= str(int(input("Year:")))
month= str(int(input("Month:")))
date= str(int(input("Date:")))
edob=[year,month,date]
print(edob)
tyear= datetime.year
tmonth= datetime.month
tday= datetime.date
cur_date=datetime(tyear, tmonth,tday)
print(cur_date)


