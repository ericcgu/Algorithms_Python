

def rotateImage(a):
    a.reverse()
    for i in range(len(a)):
        for j in range(i): 
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a

a = [[1, 2],
     [3, 4]]


print(rotateImage(a))
