#：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

import string
s = input('字符:')
strcount = 0
spacecount = 0
digitcount = 0
othercount = 0
for si in s:
    if si.isalpha():
        strcount += 1
    elif si.isspace():
        spacecount+=1 
    elif si.isdigit():
        digitcount+=1
    else:
        othercount+=1
print('{},{},{},{}'.format(strcount,spacecount,digitcount,othercount))
