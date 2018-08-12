import sys, time

# for i in range(5):
    # sys.stdout.write('{}/5\r'.format(i+1))
    # sys.stdout.flush()
#     time.sleep(1)


# for i in range(5):
    # sys.stdout.write(' ' * 10 + '\r')
    # sys.stdout.flush()
    # print(i)
    # sys.stdout.write(str(i) * (5 - i) + '\r')
    # sys.stdout.flush()
#     time.sleep(1)

strarrs = ['/','|','\\']
for i in range(15):
    sys.stdout.write(strarrs[i % 3]+'{}/15:'.format(i+1)+'#' * i+'\r')
    sys.stdout.flush()
    time.sleep(1)

