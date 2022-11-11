# List item

myList = []

myList.append('Shubel')
myList.append('Islam')
myList.append('Sunny')
myList.append(24)
myList.append(11)

print(myList[0])
print(myList[1])
print(myList[2])

print(myList[0] + ' ' + myList[1] + ' ' + myList[2])

print(myList[3])
print(myList[4])

# using for loop
print("Using for loop")
for x in myList:
    print(x)
    
    
### 3 list
Bangladesh = ['Mango', 'Banana', 'Kathal']
India = ['Egg', 'Milk', 'Doi']
Katar = ['Date-fruit', 'kaschi', 'Biriyani']

print("Please enter a food item: ")
x = input()

if x in Bangladesh:
    print(f'{x} comes from Bangladesh')
elif x in India:
    print(f'{x} comes from India')
elif x in Katar:
    print(f'{x} comes from Katar')    
else:
    print('I do not know')    