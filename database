import sqlite3

con = sqlite3.connect("library.db")
cursor = con.cursor()

def initializeDatabase():
    sqlite3.connect("library.db")
    sqlite3.connect("library.db").cursor()

    cursor.execute("Create Table If not exists bookshelf (name TEXT, writer TEXT)")
    con.commit()


def appendBook(name, writer):
    bookshelf = "Insert into bookshelf Values(?,?)"
    cursor.execute(bookshelf,(name,writer))
    con.commit()

    

def info():
    cursor.execute("Select * From bookshelf")
    data = cursor.fetchall()
    print("bookshelf tablosunun bilgileri")
    for a in data:
        print(a)


def fetchAllBooks():
    cursor.execute("Select name, writer From bookshelf")
    data = cursor.fetchall()
    print("bookshelf tablosunun bilgileri")
    for a in data:
        print(a)
