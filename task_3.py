# Task1
# Original list of favorite books
favorite_books = [
    "1984 by George Orwell",
    "To Kill a Mockingbird by Harper Lee",
    "The Great Gatsby by F. Scott Fitzgerald",
    "Pride and Prejudice by Jane Austen",
    "The Lord of the Rings by J.R.R. Tolkien",
]

# Append a new book
new_book = "The Catcher in the Rye by J.D. Salinger"
favorite_books.append(new_book)

# Remove a book
book_to_remove = "Pride and Prejudice by Jane Austen"
favorite_books.remove(book_to_remove)

# Print the updated list of favorite books
for book in favorite_books:
    print(book)


# Original list of numbers
original_numbers = [1, 2, 3, 4, 5]

# Using list comprehension to compute squares
squared_numbers = [x**2 for x in original_numbers]

# Print the list of squared numbers
print(squared_numbers)


# task2
# Tuple of weekdays
weekdays = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

# Printing the second and last days
second_day = weekdays[1]
last_day = weekdays[-1]

print("Second day:", second_day)
print("Last day:", last_day)

# List of tuples with student names and scores
student_scores = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 95),
    ("Eve", 88),
]


# Sorting the list based on scores
def get_score(student):
    return student[1]


sorted_students = sorted(student_scores, key=get_score)

# Print the sorted list of students and scores
for student in sorted_students:
    print(f"Student: {student[0]}, Score: {student[1]}")


# task3
# Creating an initial contact dictionary
contact_list = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555",
}

# Display the initial contact list
print("Initial Contact List:")
for name, number in contact_list.items():
    print(f"{name}: {number}")

# Adding a new contact
contact_list["David"] = "111-222-3333"

# Updating an existing contact
contact_list["Bob"] = "888-888-8888"

# Deleting a contact
if "Charlie" in contact_list:
    del contact_list["Charlie"]

# Display the updated contact list
print("\nUpdated Contact List:")
for name, number in contact_list.items():
    print(f"{name}: {number}")


# task4
# Creating an initial set of hobbies
favorite_hobbies = {"Reading", "Painting", "Hiking"}

# Displaying the initial set of hobbies
print("Initial Favorite Hobbies:", favorite_hobbies)

# Adding new hobbies
favorite_hobbies.add("Cooking")
favorite_hobbies.add("Gardening")

# Removing existing hobbies
favorite_hobbies.remove("Hiking")

# Displaying the updated set of hobbies
print("Updated Favorite Hobbies:", favorite_hobbies)

# Two sets of hobbies
set1 = {"Reading", "Painting", "Cooking"}
set2 = {"Painting", "Gardening", "Cooking"}

# Finding common elements between sets
common_hobbies = set1.intersection(set2)

# Displaying the common hobbies
print("Common Hobbies:", common_hobbies)


# task5
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


# Taking input from the user
num = int(input("Enter an integer: "))

# Checking if the number is prime
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
