#：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

arrup = [2,]
arrdown = [1,]
for count in range(19):
    arrup.append( arrup[count] + arrdown[count] )
    arrdown.append( arrup[count] )

sum = 0
for count in range(20):
    sum += arrup[count] / arrdown[count]
print(sum)

