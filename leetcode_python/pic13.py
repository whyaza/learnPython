#：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
#例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

from functools import reduce

for mai in range(100,1000):
    l = []
    maf = mai
    while mai :
        l.append(mai % 10)
        mai = mai // 10         #注意用地板除法
    newl = map(lambda x : x**3 ,l)             #map 函数不改变原有list,而是返回新的list
    if reduce(lambda x,y:x+y,newl) == maf:
        print(maf)
