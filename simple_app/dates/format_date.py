from datetime import datetime

datetime.

now = datetime.now()
print(now)

reformat_date = now.strftime("%d-%m-%Y T%H:%M:%S")
print(reformat_date)
print('*******************************************************')

long_month = now.strftime("%d-%B-%Y T%H:%M:%S") #B
print(long_month)

print('*******************************************************')
loong_month = now.strftime("%H:%M:%S") #B
print(loong_month)
"***********************************"
short_month = now.strftime("%d-%b-%Y T%H:%M:%S") #b
print(short_month)
print('*******************************************************')
