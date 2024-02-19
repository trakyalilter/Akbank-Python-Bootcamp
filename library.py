from _io import TextIOWrapper

class Book:
    def __init__(self, BookName, Author, ReleaseDate, Pages):
        self.BookName = BookName
        self.Author = Author
        self.ReleaseDate = ReleaseDate
        self.Pages = Pages


class Library:
    def __init__(self):
        self.BookDb = self.openlibrary()
        print("Kütüphanemize Hoş geldiniz!")
        self.mainmenu()
    def __del__(self):
        print("Library is closed!")
        self.BookDb.close()
    def mainmenu(self):
        print("""
        *** MENU***
        1) List Books
        2) Add Book
        3) Remove Book
        q) Quit
                """)
        user_input = input("Seciminiz:")
        if user_input == '1':
            self.listbooks()
        elif user_input == '2':
            self.addbook()
        elif user_input == '3':
            self.removebook()
        elif user_input == 'q' or user_input == 'Q':
            print("Tekrar görüşmek dileği ile...")
            self.closelibrary()

        else:
            print("Yanlış tuşladınız.")
            self.mainmenu()

    def addbook(self):
        book = Book(input("Kitap Adı:"), input("Kitabın Yazarı:"), input("Basım Yılı:"), input("Sayfa Sayısı:"))
        wanted_string = "%s,%s,%s,%s\n" % (book.BookName,book.Author,book.ReleaseDate,book.Pages)
        self.BookDb.write(wanted_string)
        self.mainmenu()
    def listbooks(self):
        self.BookDb.seek(0)
        kitaplistesi = self.BookDb.read().splitlines()
        print("Yazar | Kitap Adı")
        for kitap in kitaplistesi:
            _ = str(kitap).split(',')
            book = Book(_[0],_[1],_[2],_[3])
            print(f"{book.Author} | {book.BookName}")



        self.mainmenu()

    def removebook(self):
        index_of_the_book = 0
        book_name_to_remove = input("Silmek istediğiniz kitabın adı:")
        self.BookDb.seek(0)
        kitaplistesi = self.BookDb.read().splitlines()
        self.BookDb.truncate(0)
        for kitap in kitaplistesi:
            index = str(kitap).find(book_name_to_remove)
            if index != -1:
                list(kitaplistesi).remove(kitap)
                index_of_the_book_to_be_deleted = index_of_the_book
                print("Silinen Kitabın Sıra Numarası:",index_of_the_book_to_be_deleted)
            else:
                self.BookDb.write("%s\n" % kitap)
            index_of_the_book +=1
        self.mainmenu()
    @staticmethod
    def openlibrary() -> TextIOWrapper:
        f = open("books.txt", "a+", encoding="utf-8")
        f.seek(0)
        return f


    def closelibrary(self):
        del self


if __name__ == '__main__':
    lib = Library()
