#：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

    
#s = input('字符串为:')
#print(s[::-1])

def tacstr(s,l):
    if l == 0:
        return 
    print(s[l-1])
    tacstr(s,l-1)

s = input('字符串为:')
tacstr(s,len(s))
