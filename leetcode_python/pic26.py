#：利用递归方法求5!。

def jiec(n):
    if n == 1:
        return 1
    else:
        return n * jiec(n-1)

print(jiec(5))
