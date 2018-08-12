import time

#time.strftime(format[, t]) 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定。
#time localtime() 作用是格式化时间戳为本地的时间

while True:
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)

