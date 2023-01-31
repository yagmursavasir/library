from database import*

initializeDatabase()

print("""************************
kütüphane programina hosgeldiniz...

islemler:

1. Kitaplari listele
2. Kitap ara
3. Kitap ekle
Q. çikis

*****************************""")

while True:
    option = input("Yapmak istediğiniz işlemi seçiniz: ")

    if(option == "1"):
        for name,writer in fetchAllBooks():
            print(name,writer)

    elif(option == "2"):
        search = input("Aramak istediğiniz kitabin adi: ")
        for bookshelf in appendBook(name="",writer=""):
            if bookshelf == search:
                print("mecvut")
            else:
                print("mevcut değil")

    elif(option == "3"):
        bookName = input("kitabin adini giriniz: ")
        writerName = input("kitabin adini giriniz: ")
        appendBook(name=bookName,writer=writerName)

    elif(option == "q" or option == "Q"):
        print("yeniden bekleriz...")
        break

    else:
        print("hatali islem yaptiniz...")
        
