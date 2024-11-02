while True:
    print("""
            1.Add book
            2.Update book
            3.Remove book
            4.View All books
            5.Search book
            6.Exit
            
        """)
    c=int(input("select an option:"))
    if c==1:
        l=int(input("how many books :"))
        book=[]
        for i in range(1,l+1):
            print('number of books :',i)
            snum=input("enter the book number :")
            sname=input("enter the book name :")
            book.append({'name':sname,'book number':snum})
        print(book)

    elif c==2:
        l=int(input("enter the limit :"))
        book=[]
        for i in range(1,l+1):
            print('number of books :',i)
            snum=input("enter the book number :")
            sname=input("enter the book name :")
            book.append({'name':sname,'book number':snum})
        print(book)

# elif c==3:
# d= {1: 'abhi', 2: 'vinayak', 3: 'akshay'}
