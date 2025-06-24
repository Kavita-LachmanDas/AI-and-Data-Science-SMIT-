# Library Management System
# Book : Book Information, Availability Check, Borrow, Return
# Library :
# Person: | Patron


class Book:
  def __init__(self,title,author,genre,ISBN):
    self.title = title
    self.author = author
    self.genre = genre
    self.ISBN = ISBN
    self.status = True

  def book_info(self):
    return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nISBN: {self.ISBN}"

  def check_status(self):
    if self.status:
      return "Available"
    else:
      return "Not Available"

  def borrow_book(self):
    if self.status:
      self.status = False
      return f"You have successfully borrowed {self.title}"
    else:
      return f"{self.title} is not available"

  def return_book(self):
    self.status = True
    return f"You have successfully returned {self.title}"
  


class Person:
  def __init__(self, name, pid):
    self.name = name
    self.pid = pid
    self.borrowed_books = {}

  def personinfo(self):
    return f"Person Name: {self.name}\n ID is: {self.pid}"

  def borrow_book(self,book):
    if book.check_status() == "Available":
      self.borrowed_books[book] = book.borrow_book()
      return self.borrowed_books[book]
    else:
      return f"Sorry, the book is not available"

  def return_book(self,book):
    if book in self.borrowed_books:
      self.borrowed_books[book] = book.return_book()
      return self.borrowed_books[book]
    else:
      return "You haven't borrowed this book"
    
class Library:
  def __init__(self):
    self.books = []
    self.persons = []

  def add_book(self,book):
    self.books.append(book)

  def add_person(self,person):
    self.persons.append(person)

  def remove_book(self,book):
    if book in self.books:
      self.books.remove(book)
    else:
      return "Book not Found"
  def list_books(self):
    for book in self.books:
      print(book.book_info())


# Creation of System

book1 = Book("RichvsPoorDad","Paul","Motivation","N09244")
book2 = Book("20in80Rule","Archer","ScienceFiction","N08338")
book3 = Book("The Silent Patient","Paul Noeschi","Truama&Suspense","N08997")

person1 = Person("Mehwish","P0011")
person2 = Person("Areeba","P0022")

sallibrary = Library()
sallibrary.add_book(book1)
sallibrary.add_book(book2)
sallibrary.add_book(book3)
sallibrary.add_person(person1)
sallibrary.add_person(person2)


print(person1.borrow_book(book3))          