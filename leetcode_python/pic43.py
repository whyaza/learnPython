def add(x,y):
    c = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    for i in range(len(x)):
        for j in range(len(x[i])):
            c[i][j] = x[i][j] + y[i][j]
    return c

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

rs = add(X,Y)
for r in rs:
    print(r)
