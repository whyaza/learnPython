#：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

# l = []
# for i in range(2,1000):
    # isSu = True
    # for j in range(2,i):
        # if i % j == 0:
            # isSu = False
    # if isSu is True:
        # l.append(i)

# ma = int(input('ma:'))
# ck = [0] * 1000     #列表初始化
# inx = 0
# while ma != 1:
    # if (ma % l[inx]) == 0:
        # ck[inx] += 1
        # ma //= l[inx]
    # else:
        # inx += 1

# for i in range(0,1000):
    # if ck[i] != 0:
#         print(str(l[i]) * ck[i],' ',end=',')

def reduceNum(n):
    print('{} = '.format(n))
    if not isinstance(n,int) or n <= 0:
        print('请输入正确的正整数')
    elif n in [1]:
        print('{}'.format(n))
    while n != 1:
        for index in range(2,n+1):
            if n % index == 0:
                n //= index
                print('{}*'.format(index))
                break

reduceNum(90)
reduceNum(100)
