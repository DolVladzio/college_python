#========================================
import list_of_books
#========================================
class Library:
    def __init__(self, book_name):
        self.book_name = book_name

    def SearchBook(self):
        try:
            i = 0
            found_book = False
            while i < len(list_of_books.library_books):
                first_value = next(iter(list_of_books.library_books[i].values()))

                if first_value == self.book_name:
                    print("-------------------------------------")
                    for key, value in list_of_books.library_books[i].items():
                        print(f"| {key}: {value}")
                    found_book = True
                    break
                i += 1

            if not found_book:
                print("-------------------------------------")
                print(f"| Book: '{self.book_name}' isn't in the library")
        except Exception as error:
            print(f"| An error occurred: {error}")
        
        return "-------------------------------------"
        
    def AddBook(self, addBookName, addBookYear, addBookAuthor):
        try:
            w = 0
            add_book = False
            while w < len(list_of_books.library_books):
                add_value = next(iter(list_of_books.library_books[w].values()))
                #========================================
                if add_value != addBookName:
                    print("-------------------------------------")
                    print(f"| Book: '{addBookName}' - was added")
                    for key, value in list_of_books.library_books[w].items():
                        list_of_books.library_books[w].update({"name": addBookName,
                                                               "year": addBookYear,
                                                               "author": addBookAuthor})

                    add_book = True
                    #_Show list of books=====================
                    i = 0
                    while i < len(list_of_books.library_books):
                        print("-------------------------------------")
                        for key, value in list_of_books.library_books[i].items():
                            print(f"| {key}: {value}")
                        i += 1
                    return "-------------------------------------"
                    #========================================
                w += 1
            #========================================
            if not add_book:
                print("-------------------------------------")
                return f"| Book: '{self.book_name}' has already added to the library"
        except Exception as error:
            print(f"| An error occurred: {error}")

    def DeleteBook(self):
        try:
            x = 0
            delete_book = False
            while x < len(list_of_books.library_books):
                delete_value = next(iter(list_of_books.library_books[x].values()))
            #========================================
                if delete_value == self.book_name:
                    print(f"| Book: '{delete_value}' - was deleted")
                    for key, value in list_of_books.library_books[x].items():
                        del list_of_books.library_books[x]    

                    delete_book = True
                    break
                x += 1
            #========================================
            if not delete_book:
                print("-------------------------------------")
                print(f"| Book: '{self.book_name}' there isn't in the library")
        except Exception as error:
            print(f"| An error occurred: {error}")
                
        return (self.SearchBook())
#_Objects================================
library_object = Library("Hello World")
#_Result=================================
print(library_object.SearchBook())

print(library_object.AddBook("Hello World", 2021, "Vladzio Dolynka"))

print(library_object.DeleteBook())
#========================================