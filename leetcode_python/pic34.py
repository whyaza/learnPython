#：文本颜色设置。

class bcolors:      #可以是控制台变色
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    
print(bcolors.HEADER + 'header tags')
print(bcolors.OKBLUE + 'ok tags')
