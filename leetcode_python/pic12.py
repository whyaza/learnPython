#：判断101-200之间有多少个素数，并输出所有素数。

count = 0
for i in range(101,201):
    isSu = True
    for j in range(2,i):
        if i % j == 0:
            isSu = False
            break
    if isSu == True:
        print(i)
        count += 1
print("count:",count)

