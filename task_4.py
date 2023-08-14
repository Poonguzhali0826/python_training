#1 Create a Python class named Student with attributes name and age, and instantiate an object with the name 'John' and age 20.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate an object of the Student class
john = Student(name='John', age=20)

# Access the attributes of the object
print("Name:", john.name)
print("Age:", john.age)



#2 Define a base class Shape with a method area(). Create a class Circle and Rectangle that inherits from Shape and calculates the area using a given radius.
import math

class Shape:
    def area(self):
        pass  # This method will be overridden by subclasses

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Creating Circle and Rectangle objects
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)

# Calculating and printing the areas
print("Circle Area:", circle.area())
print("Rectangle Area:", rectangle.area())


#3 Write a function print_area(shape) that takes an instance of Shape (with an area() method) and prints its area.
 
def print_area(shape):
    if isinstance(shape, Shape):
        print("Area:", shape.area())
    else:
        print("Invalid shape instance.")

# Creating Circle and Rectangle objects
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)

# Calling the print_area function
print_area(circle)
print_area(rectangle)

#4 Create a BankAccount class with a private attribute balance. Implement a balance property that allows getting and setting the balance, ensuring it's never negative.

class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Invalid balance. Balance cannot be negative.")

# Creating a BankAccount object
account = BankAccount(initial_balance=1000)

# Getting the balance using the balance property
print("Current Balance:", account.balance)

# Setting a new balance using the balance property
account.balance = 1500
print("Updated Balance:", account.balance)

# Trying to set a negative balance
account.balance = -200


#5 Build a Library class that contains a list of Book instances. Implement a method to add a book and another method to display all books in the library.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added '{book.title}' by {book.author} to the library.")
        else:
            print("Invalid book instance.")

    def display_books(self):
        print("Books in the library:")
        for book in self.books:
            print(f"'{book.title}' by {book.author}")

# Creating a Library object
library = Library()

# Adding books to the library
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Displaying all books in the library
