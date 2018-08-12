#求区间内素数:

begin = int(input('起始区间:'))
end = int(input('终止区间:'))
for digit in range(begin,end):          # for ... else ...
    for idx in range(2,digit//2 + 1):
        if digit % idx == 0:
            break
    else:
        print(digit)
