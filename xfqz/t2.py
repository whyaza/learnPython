def fun(n , *args) :
    print(n)
    print(args)     #未拆包
    print(*args)    #进行拆包
fun(1,2,3,4)

def fun(**kwargs):
    print(kwargs)   #未拆包
    print(*kwargs)  #进行拆包
fun(a=1,b=2)
