from collections import defaultdict
from datetime import datetime, timedelta

class StudentDataBaseException(Exception): pass
class NoStudent(StudentDataBaseException): pass
class NoBook(StudentDataBaseException): pass

"""To keep of a record of students 
 who have yet to return books and their due dates"""
class CheckedOut:
     loan_period = 10
     fine_per_day = 2

     def __init__(self):
         self.due_dates = {}

     def check_in(self, name):
          due_date = datetime.now() + timedelta(days=self.loan_period)
          self.due_dates[name] = due_date

     def check_out(self, name):
         current_date = datetime.now()
         if current_date > self.due_dates[name]:
             delta = current_date - self.due_dates[name]
             overdue_fine = self.fine_per_day * delta.days
             print("Fine Amount: ", overdue_fine)

# This only contains the title name for now
class BookStatus:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title

    def __hash__(self):
        return 0

    def __eq__(self, other):
        return self.title == other

# contains a set of books
class Library:
    record = CheckedOut()

    def __init__(self):
        self.books = set()

    def add_book(self, new_book):
        self.books.add(new_book)

    def display_books(self):
        if self.books:
            print("The books we have made available in our library are:\n")
            for book in self.books:
                print(book)
        else:
            print("Sorry, we have no books available in the library at the moment")

    def lend_book(self, requested_book):
        if requested_book in self.books:
            print(f'''You have now borrowed \"{requested_book}\"''')
            self.books.remove(requested_book)
            return True

        else:
            print(f'''Sorry, \"{requested_book}\" is not there in our library at the moment''')
            return False

# container for students
class StudentDatabase:
    def __init__(self):
        self.books = defaultdict(set)

    def borrow_book(self, name, book, library):
        if library.lend_book(book):
            self.books[name].add(book)
            return True
        return False

    def return_book(self, name, book, library):
        if book not in self.books[name]:
            raise NoBook(f'''\"{name}\" doesn't seem to have borrowed "{book}"''')
            return False
        else:
            library.add_book(book)
            self.books[name].remove(book)
            return True

    def students_with_books(self):
        for name, books in self.books.items():
            if books:
                yield name, books


def borrow_book(library, book_tracking):
    name = input("Student Name: ")
    book = BookStatus(input("Book Title: "))

    if book_tracking.borrow_book(name, book, library):
        library.record.check_in(name)

def return_book(library, book_tracking):
    name = input("Student Name: ")
    returned_book = BookStatus(input("Book Title: "))

    if book_tracking.return_book(name, returned_book, library):
        library.record.check_out(name)


line = "_" * 100
menu = "Library Management System \n\n \
1) Add Book \n \
2) Display all Books \n \
3) Borrow a Book \n \
4) Return a Book \n \
5) Lending Record \n \
6) Exit"

library = Library()
book_tracking = StudentDatabase()

while True:
    print(line)
    print(menu)

    choice = get_valid_choice(min=1, max=6)
    print(line)

    if choice == 1:
        library.add_book(BookStatus(input("Book Title: ")))

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        borrow_book(library, book_tracking)

    elif choice == 4:
        return_book(library, book_tracking)

    elif choice == 5:
        students = tuple(book_tracking.students_with_books())
        if students:
            for name, book in students:
                print(f"{name}: {book}")
        else:
            print("No students have borrowed books at the moment")

    elif choice == 6:
        break
