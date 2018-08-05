import csv

with open('data.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerow(['10001','Mike',20])
    writer.writerow(['10002','John',21])
    writer.writerow(['10003','diss',45])
