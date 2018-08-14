import random

te = [1,2,3,4]
cou = 1
for i in te:
    print(i)
    if random.randint(1,100) > 50:
        te.append(5)
    print('cou:',cou)
