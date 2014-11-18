class Library(object):
  def __init__(self, shelves):
    self.shelves = shelves

  def add_shelf(self, shelf):
    self.shelves.append(shelf)

  def list_books_as_string(self):
    book_list = ""
    for shelf in self.shelves:
      book_list += shelf.label + " contains:\n" + shelf.list_of_books() + "\n"
    if len(book_list) == 0:
      return "There are no shelves in the library."
    else:
      return book_list

class Shelf(object):
  def __init__(self, books, label):
    self.books = books
    self.label = label

  def add_book(self, book):
    self.books.append(book)

  def remove_book(self, book):
    if book in self.books:
      self.books.remove(book)

  def list_of_books(self):
    book_list = ""
    for book in self.books:
      book_list += book.describe() + "\n\n"
    if len(book_list) == 0:
      return "There are no books on this shelf."
    else:
      return book_list

class Book(object):
  def __init__(self, title, author, page_count):
    self.title = title
    self.author = author
    self.page_count = page_count
    self.shelf = None

  def describe(self):
    return "title: "+ self.title + "\nauthor: " + self.author
    + "\nLength: " + str(self.page_count) + " pages"

  def enshelf(self, shelf):
    if self.shelf == None:
      shelf.add_book(self)
      self.shelf = shelf

  def unshelf(self):
    if self.shelf:
      self.shelf.remove_book(self)
      self.shelf = None


