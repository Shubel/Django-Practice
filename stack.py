books = []

books.append('Learn C')
books.append('Learn C++')
books.append('Learn C#')
print(books)

books.pop()
print(books)
print('Now the top book is : ', books[-1])

books.pop()
print(books)
print ('Now the top book is : ', books[-1])

books.pop()
# print(books)
if not books:
    print('No books are left')