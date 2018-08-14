def fun1(ss):
    if ss == 'sb':
        return 'yes'
    if ss == 'dg':
        return 'no'
    if ss== 'lp':
        return 'default'

print(fun1('sb'))
print(lambda x: fun1('sb'))
print((lambda :fun1('sb'))())

print(fun1)
