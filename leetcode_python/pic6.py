#题目：斐波那契数列。

#程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

#在数学上，费波那契数列是以递归的方法来定义：

#F0 = 0     (n=0)
#F1 = 1    (n=1)
#Fn = F[n-1]+ F[n-2](n=>2)

def fibo(n):
    a, b = 1, 1
    for i in range(n-1):
        a , b = b , a +b
    return a

#print(fibo(10))

def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

print(fib(10))

test = [1,7,8,2,234,32]
print(test[-1])
print(test[-2])

print(test[2:5:1])
print(test[5:2:-1])
