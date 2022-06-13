books={'book1':100,'book2':150,'book3':200}
print("Books :",books)
newbook=input("Enter the book to add: ")
n=int(input("Enter the number of stocks: "))
books.update({newbook:n})
print("Updated Books :",books)
x=input("Enter the book to delete : ")
element=books.pop(x)
print("Newly Updated Books :",books)
