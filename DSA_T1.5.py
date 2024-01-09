def arrayMax(a,n):
    currentMax = a[0]
    for i in range(1,n):
        if (a[i] > currentMax):
            currentMax = a[i]
    return currentMax

num = [1,55,32,7,85,32,2]

print(arrayMax(num,7))