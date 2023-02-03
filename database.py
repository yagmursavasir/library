import sqlite3

con = sqlite3.connect("library.db")
cursor = con.cursor()

cursor.execute(
    "create table if not exists library(name TEXT,writer TEXT)")
con.commit()

def initializeDatabase():
    sqlite3.connect("library.db")
    sqlite3.connect("library.db").cursor()

    cursor.execute("Create Table If not exists bookshelf (name TEXT, writer TEXT)")
    con.commit()

while True:
    ##### Book List #####
    def listBook():
        cursor.execute("select * from library")
        listBook = cursor.fetchall()
        print("kitap listesi: ")
        for i in listBook:
            print(i)

    ##### Add Book #####

    def addBook(name,writer):
        cursor.execute("insert into library values(@p1 , @p2"),(name,writer)
        cursor.commit()

    #### Delete Book ###

    def deleteBook(name):
        cursor.execute("delete from library where name=@p1")
        cursor.commit()


# def appendBook(name, writer):
#     bookshelf = "Insert into bookshelf Values(?,?)"
#     cursor.execute(bookshelf,(name,writer))
#     con.commit()

    

# def info():
#     cursor.execute("Select * From bookshelf")
#     data = cursor.fetchall()
#     print("bookshelf tablosunun bilgileri")
#     for a in data:
#         print(a)


# def fetchAllBooks():
#     cursor.execute("Select name, writer From bookshelf")
#     data = cursor.fetchall()
#     print("bookshelf tablosunun bilgileri")
#     for a in data:
#         print(a)
