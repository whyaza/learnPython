#：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

from functools import reduce
for di in range(3,1001):
    yins = []
    if di % 2 == 0:
        for i in range(1, di//2 + 1):
            if di % i == 0:
                yins.append(i)
    if len(yins) != 0:
        if reduce(lambda x,y:x+y,yins) == di:
            print(di)


