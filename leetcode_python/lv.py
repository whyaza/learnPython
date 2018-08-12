a = float(input('a:'))
b = float(input('b:'))
lv = (a / b)*100
print('|',end='')
for count in range(1,101):
    if count < lv :
        print('#',end='')
    else:
        print('.',end='')
print('|',end='')
