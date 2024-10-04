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
