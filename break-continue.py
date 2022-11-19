# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    # count = count + 1
    count += 1
    if count >= 50:
        break
    
print('sunny')

# Prints out only odd numbers -> 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
    
    
#### break
i = 1
while i <= 20:
    if i == 10:
        break
    print(i)
    i += 1
    # if i == 10:
    #     break

print('Hello')


#### continue
i = 1
while i <= 30:
    # if i == 25:
    #     continue
    print(i)
    i += 1
    if i == 25:
        continue

print('Hello')