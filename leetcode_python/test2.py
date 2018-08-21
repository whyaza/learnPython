理解装饰器的前提:1.所有东西都是对象(函数可以当做对象传递)  2.闭包
闭包的概念
1）函数嵌套
2）内部函数使用外部函数的变量  
3）外部函数的返回值为内部函数

def test(name):
    def test_in():
        print(name)
    return test_in

func = test('whyz')
func()

装饰器的原型
import time
def showtime(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('spend is {}'.format(end_time - start_time))

    return wrapper

def foo():
    print('foo..')
    time.sleep(3)

foo = showtime(foo)
foo()

不带参数的装饰器(装饰器,被装饰函数都不带参数)
import time
def showtime(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('spend is {}'.format(end_time - start_time))

    return wrapper

@showtime  #foo = showtime(foo)
def foo():
    print('foo..')
    time.sleep(3)

@showtime #doo = showtime(doo)
def doo():
    print('doo..')
    time.sleep(2)

foo()
doo()

带参数的被装饰函数
import time
def showtime(func):
    def wrapper(a, b):
        start_time = time.time()
        func(a,b)
        end_time = time.time()
        print('spend is {}'.format(end_time - start_time))

    return wrapper

@showtime #add = showtime(add)
def add(a, b):
    print(a+b)
    time.sleep(1)

@showtime #sub = showtime(sub)
def sub(a,b):
    print(a-b)
    time.sleep(1)

add(5,4)
sub(3,2)

带参数的装饰器(装饰函数)
import time
def time_logger(flag = 0):
    def showtime(func):
        def wrapper(a, b):
            start_time = time.time()
            func(a,b)
            end_time = time.time()
            print('spend is {}'.format(end_time - start_time))
            
            if flag:
                print('将此操作保留至日志')

        return wrapper

    return showtime

@time_logger(2)  #得到闭包函数showtime,add = showtime(add)
def add(a, b):
    print(a+b)
    time.sleep(1)

add(3,4)
实际是对原有装饰器的一个函数的封装,并返回一个装饰器(一个含有参数的闭包函数),
当使用@time_logger(3)调用的时候,Python能发现这一层封装,并将参数传递到装饰器的环境去

类装饰器 : 一般依靠类内部的__call__方法
import time
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        start_time = time.time()
        self._func()
        end_time = time.time()
        print('spend is {}'.format(end_time - start_time))

@Foo  #bar = Foo(bar)
def bar():
    print('bar..')
    time.sleep(2)

bar()

装饰器的缺点:1.位置错误的代码->不要在装饰器之外添加逻辑功能
3.不能装饰@staticmethod 或者 @classmethod已经装饰过的方法
2.装饰器会对原函数的元信息进行更改,比如函数的docstring,__name__,参数列表:
t1
import time
def showtime(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('spend is {}'.format(end_time - start_time))

    return wrapper

@showtime  #foo = showtime(foo)
def foo():
    print('foo..')
    time.sleep(3)

def doo():
    print('doo..')
    time.sleep(2)

print(foo.__name__)
print(doo.__name__)

t2
import time
from functools import wraps
def showtime(func):

    @wraps(func)    #wraps本身也是一个装饰器,他能把函数的元信息拷贝到装饰器函数中
    #使得装饰器函数与原函数有一样的元信息
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('spend is {}'.format(end_time - start_time))

    return wrapper

@showtime  #foo = showtime(foo)
def foo():
    print('foo..')
    time.sleep(3)

def doo():
    print('doo..')
    time.sleep(2)

print(foo.__name__)
print(doo.__name__)

常用的内置装饰器:
1.staticmethod: 类似实现了静态方法 注入以后,可以直接 :  类名.方法
2.property:经过property装饰过的函数 不再是一个函数,而是一个property
类似实现get,set方法,相当于语法糖
test:
@property
def width(self):
    return self.__width

@width.setter
def width(self, newWidth):
    self.__width = newWidth
3.classmethod: 与staticmethod很相似,貌似就只有这一点区别:
第一个参数需要是表示自身类的 cls 参数，
可以来调用类的属性，类的方法，实例化对象等。

