# This prints out "John is 23 years old."
name = 'John'
age = 23

print('%s is %d years old' %(name, age))




# This prints out: A list: [1, 2, 3]
myList = [1,2,3]

print("A list: %s" % myList)




# That prints out 12, because "Hello world!" is 12 characters long, including punctuation and spaces.
aString = "Hello world!"

print("single quotes are ' '")
print(aString)
print(len(aString))




# How to find index number
aString = "Hello world!"

print(aString.index("w"))
print(aString[6])





###exercise
aString = "Hello world"

### Word/Letter Count
print(aString.count("l"))
print(aString.count("o"))

##word/letter slice
print(aString[3:7])
print(aString[1:5])
print(aString[:4])
print(aString[1:])
print(aString[-3:])
print(aString[-5:])





