# while True:
#     print("""
#             1.Add book
#             2.Update book
#             3.Remove book
#             4.View All books
#             5.Search book
#             6.Exit
            
#         """)
#     c=int(input("select an option:"))
#     if c==1:
#         l=int(input("how many books :"))
#         book=[]
#         for i in range(1,l+1):
#             print('number of books :',i)
#             snum=input("enter the book number :")
#             sname=input("enter the book name :")
#             book.append({'name':sname,'book number':snum})
#         print(book)

#     elif c==2:
#         l=int(input("enter the limit :"))
#         book=[]
#         for i in range(1,l+1):
#             print('number of books :',i)
#             snum=input("enter the book number :")
#             sname=input("enter the book name :")
#             book.append({'name':sname,'book number':snum})
#         print(book)

#------------------------------------------------------------------------------------#

library=[]
def addbook():
    book_name=input("enter book name :")
    writer=input("enter the writername :")
    year=int(input("enter the year :"))
    library.append({
        "name":book_name,
        "writer":writer,
        "year":year

    })
    print("book added successfully")

def updatebook():
    book_name=input("enter the book name to update")
    for book in library:
        if book["name"]==book_name:
            book["writer"]= input("enter new writer")
            book["year"]=int(input("enter the year"))
            print("book updated successfully")
            return
        print("book not found")

def removebook():
    book_name=input("enter the bookname to ramove")
    for book in library:
        if book["bookname"]==book_name:
            library.remove(book)
            print("book removed successfully")
            return
    print("book not found")

def view_book():
    if library:
        print("list of all books")
        for book in library:
            print(f"name:{book['name']},writer:{book['writer']},year:{book['year']}")
            print()
    else:
        print("no books in library")


def main():
    print("welcome to library")
    while True:
        print("""
                1.add book
                2.update book
                3.remove book
                4.view book
                5.exit
              """)
        choice=input("select any: ")
        
        if choice==1:
            addbook()
        elif choice==2:
            updatebook()
        elif choice==3:
            removebook()
        elif choice==4:
            view_book()
        elif choice==5:
            print("exit the library")
            break
        else:
            print("invalid")

main()
