num = [1,55,32,7,85,32,2]

largest = 0
second = 0

for i in num:
    if i > largest:
        second = largest
        largest = i

    elif i > second:
        second = i
        
print(largest)
print(second)
