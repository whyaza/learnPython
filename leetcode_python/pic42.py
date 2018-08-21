num = 2
def autofunc():
    num = 1
    print('internal block num is',num)
    num += 1

for i in range(3):
    print('the num is ',num)
    num += 1
    autofunc()
