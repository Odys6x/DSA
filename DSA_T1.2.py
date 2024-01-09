num = [1,55,32,7,85,32,2]
count = len(num)
half = int(len(num)/2)

for i in range(half):
    temp = num[i]
    num[i] = num[count - 1]
    num[count - 1] = temp
    count-=1

print(num)