#List item

myList = []

myList.append('Shubel')
myList.append('Islam')
myList.append('Sunny')
myList.append(24)
myList.append(11)

print(myList)

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
    
print('Hello')
    
    
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
    



### In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable. You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator []. Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.


# numbers = []
# strings = []
# names = ["John", "Eric", "Jessica"]

# # write your code here
# second_name = None

# # this code should write out the filled arrays and the second name in the names list (Eric).
# print(numbers)
# print(strings)
# print("The second name on the names list is %s" % second_name)

numbers =[]
strings = []
names = ["John", "Eric", "Jessica"]

#write code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append('hello')
strings.append('world')

second_name = names[1]

print(numbers)
print(strings)
print('The second name on the names list is %s' % second_name) ###The second name on the names list is Eric


###example
subjects = ['Python', 'Java', 'PHP', 'C', 'C++']

print(subjects)
print(subjects[0])
print(subjects[4])
print(subjects[2:])
print(subjects[-1:])
print(subjects[1:4])

print(subjects + ['Javascript'])
print(subjects + ['C#'])
print(subjects + ['Javascript', 'C#'])

# 'in' and 'not in' operator
print('Python' in subjects)
print('Python' not in subjects)
print('C#' not in subjects)