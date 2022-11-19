# 1 + 2 + 3 + . . . . + n

n = int(input('Enter the last number: '))

sum = 0
for x in range(1, n+1, 1):
    sum = sum + x
print(sum)
    



# 2 + 4 + 6 + . . . . + n

n = int(input('Enter the last number: '))

sum = 0
for x in range(2, n+1, 2):
    sum = sum + x
print(sum)
