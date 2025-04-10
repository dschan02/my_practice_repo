# Demetrius Schank
# Exam 2 Part 2 Tester
# Date: 1/30/2025

from book import Book   #imports class Book from book.py

books = []
with open("books.txt") as file:
    for line in file:
        file_info = line.strip().split(',')     #creates list
        book_obj = Book(file_info[0], file_info[1], file_info[2])
        books.append(book_obj)
        print(book_obj)

# call (and print?) last four methods on first book
print("Step 3:")
print(books[0].get_title())
print(books[0].get_author())
print(books[0].get_genre())
print(books[0].is_checked_out())

# check out and return the first book
print("Checking out and returning book:")
books[0].check_out()
print(books[0])
books[0].return_book()
print(books[0])




