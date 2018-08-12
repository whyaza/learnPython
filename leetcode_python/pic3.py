#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
#:若一个数能表示成某个整数的平方的形式，则称这个数为完全平方数

#:x+100 = m *m   x +100 +168 = n * n

xi = [i*i-100 for i in range(1,1000)]
yi = [i*i-268 for i in range(1,1000)]
for i in xi:
    for j in yi:
        if i ==j :
            print(i)

