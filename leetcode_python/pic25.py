#：求1!+2!+3!+...+20!的和。

sum = 1
jiec = 1
for count in range(2,21):
    jiec = jiec*count
    sum += jiec 
print(sum)

