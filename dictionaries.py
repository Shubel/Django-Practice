studentID = {
    '101' : 'Salman Khan',
    '102' : 'Amir Khan',
    '103' : 'Imran Khan',
}

print(studentID['101'])
print(studentID.get('102'))
print(studentID.get('104', 'Not a valid number'))
print(studentID.get('104'))
