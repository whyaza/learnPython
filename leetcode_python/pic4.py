#输入某年某月某日，判断这一天是这一年的第几天？

year = int(input('年:'))
month = int(input('月:'))
day = int(input('日:'))
months = (0,31,28,31,30,31,30,31,31,30,31,30,31)

count=0
if (year%400 == 0) or ((year%4==0) and (year%100!=0)):
    if month > 2:
        count += 1
count += day
month -= 1
while 0 < month <= 12:
    count += months[month]
    month -= 1

print(count)
    

