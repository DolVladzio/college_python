#_OOP
#=========================================================
#_Task_1
class Book:
    #_Constructor
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
    #_Method-1
    def nameOfBook(self):
        return f"- Name of book: {self.name}"
    #_Method-2
    def authorOfBook(self):
        return f"- Author of book: {self.author}"
    #_Method-3
    def yearOfBook(self):
        return f"- Year of publication: {self.year}"
#=========================================================
#_Task_2
class EBook(Book):
    #_Constructor
    def __init__(self, filesize):
        self.filesize = filesize
    #_Method-1
    def getFileSize(self):
        size_type = "mb"
        return f"- Size of file: {self.filesize}{size_type}"
#=========================================================
#_Task_3
class PaperBook(Book):
    #_Constructor
    def __init__(self, weight):
        self.weight = weight
    #_Method-1
    def paperBook(self):
        weight_type = "kg"
        return f"- Weight of book: {self.weight}{weight_type}"
#=========================================================
#_Task_4
class BorrowAble(abc.ABC):
    @abc.abstractmethod
    #_Abstract method-1
    def borrowBook(self): pass
    #_Abstract method-2
    def returnBook(self): pass
#=========================================================
#_Task_5
class Library(BorrowAble):
    #_List of books
    books_list = [
        "Surgeon",
        "Assistant",
        "Sinful",
        "Double",
        "Deathly",
        "Mephisto Club",
        "Keepers of Death",
        "Killing cold",
        "The girl who is silent",
        "The Last One to Die",
        "Die Again",
        "I know a secret",
        "Listen to me"
    ]
    #_Constructor-1
    def __init__(self, nameOfBook):
        self.nameOfBook = nameOfBook
    #_Method-1
    def addBook(self): return f"- The book '{self.nameOfBook}' has just added"
    #_Destructor-2
    def __del__(self): return f"- The book '{self.nameOfBook}' has just removed\n- Error 12596: 'You don't have a permission'\n"
    #_Method-2(Displaying the random book from 'library')
    def borrowBook(self):
        #_Choosing a random number of book
        numberOfBook = self.books_list[(random.randint(1, len(self.books_list))) - 1]
        return f"- The book '{numberOfBook}' has already borrowed"
    #_Method-3(Displaying the random book from 'library')
    def returnBook(self)
        #_Choosing a random number of book
        numberOfBook = self.books_list[(random.randint(1, len(self.books_list))) - 1]
        return f"- The book '{numberOfBook}' has already returned"
#=========================================================
#_Task_6
class Member():
    #_List of members
    members_list = [
        "Bernard Arnault",
        "Elon Musk",
        "Larry Ellison",
        "Mark Zuckerberg",
        "Bill Gates"
    ]
    #_Constructor-1
    def __init__(self, nameOfMember):
        self.nameOfMember = nameOfMember
    #_Method-1
    def addMember(self): return f"- The member '{self.nameOfMember}' has just added"
    #_Destructor-2
    def __del__(self): return f"- The member '{self.nameOfMember}' has just removed. Error 12596: 'You don't have a permission'\n"
    #_Method-2(Displaying the random member from list)
    def registerMember(self):
        #_Choosing a random number of member
        numberOfMember = self.members_list[(random.randint(1, len(self.members_list))) - 1]
        return f"- The member '{numberOfMember}' has already registered to library"
    #_Method-3(Displaying the random member from list)
    def cancelMember(self):
        #_Choosing a random number of member
        numberOfMember = self.members_list[(random.randint(1, len(self.members_list))) - 1]
        return f"- The member '{numberOfMember}' has already removed from library"
#=========================================================
#_Task_9(Output)
book_object = Book("Listen me", "Tess Gerritsen", 2022)
ebook_object = EBook(1024)
paper_book_object = PaperBook(1.5)
library_object = Library("Just book")
member_object = Member("John Doe")
#_Book=========================================================
print(book_object.nameOfBook())
print(book_object.authorOfBook())
print(book_object.yearOfBook())
endLine()
#_EBook===================================================
print(ebook_object.sizeOfEbook())
endLine()
#_Paper===================================================
print(paper_book_object.weightOfBook())
endLine()
#_Library=================================================
print(library_object.addBook())
print(library_object.__del__())
print(library_object.borrowBook())
print(library_object.returnBook())
endLine()
#_Member==================================================
print(member_object.addMember())
print(member_object.__del__())
print(member_object.registerMember())
print(member_object.cancelMember())
endLine()
#=========================================================
