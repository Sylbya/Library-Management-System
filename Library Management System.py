class Library:
    def __init__(self):
        self.books = []

    def add_book(self, new_book):
        self.books.append(new_book)

    def display_books(self):
        if self.books:
            print("The books we have made available "
                  "in our library are:\n")
            for book in self.books:
                print(book)
        else:
            print("Sorry, we have no books available "
                  "in the library at the moment")

    def lend_book(self, requested_book):
        print(f"You have now borrowed '{requested_book}'")
        self.books.remove(requested_book)


class Student:
    def __init__(self, name, book):
        self.name = name
        self.borrowed_books = []
        self.borrowed_books.append(book)

    def borrow_book(self, name):
        self.borrowed_books.append(name)

    def return_book(self, book):
        self.borrowed_books.remove(book)
        print(f"You have successfully returned '{book}'")


def find_student(students, name):
    for student in students:
        if name == student.name:
            return student
    return "Not Found"


def borrow_book(student_name, book_name):
    if book_name not in library.books:
        print("Book not found in library")
        return

    library.lend_book(book_name)
    student = find_student(students, student_name)
    if student == "Not Found":
        students.append(Student(student_name, book_name))
    else:
        student.borrow_book(book_name)


def return_book(student_name, book_name):
    student = find_student(students, student_name)
    if student == "Not Found":
        print("Student not Found in database")
        return
    if book_name not in stuent.borrowed_books:
        print("Book not found in database")
        return
    student.return_book(book_name)
    library.add_book(book_name)


def display_active_loans():
    has_active_loans = False
    for student in students:
        if student.borrowed_books:
            has_active_loans = True
            print(student.name, ": ",
                  ', '.join(student.borrowed_books))
    if not has_active_loans:
        print("No active loans")


library = Library()
students = []
line = '_' * 100
menu = """Library Management System \n
1) Add Book
2) Display all Available Books
3) Lend a Book
4) Return a Book
5) Display list of students who have borrowed
6) Exit \n"""

while True:
    print(line)
    print(menu)

    choice = int(input("Choice: "))
    print(line)

    if choice == 1:
        library.add_book(input("Book Name: "))

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        student_name = input("Student Name: ")
        book_name = input("Book Name: ")
        borrow_book(student_name, book_name)

    elif choice == 4:
        student_name = input("Student Name: ")
        book_name = input("Book Name: ")
        return_book(student_name, book_name)

    elif choice == 5:
        display_active_loans()

    elif choice == 6:
        break

    else:
        print("Invalid Choice")

