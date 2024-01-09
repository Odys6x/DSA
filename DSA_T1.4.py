num = [2, 4, 6, 8, 10]
value = int(input("Enter a number: "))

for count, i in enumerate(num):
    if value > i:
        num.insert(count + 1, value)
        break

print(num)
