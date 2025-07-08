
#  Challenge: Library Book Tracker
# Write a function called library_tracker that:

# 1️⃣ Takes a list of dictionaries.
# Each dictionary represents a book with these keys:

# 'title': book title

# 'author': author name

# 'available_copies': integer (number of copies currently available)

# 'borrowed': list of strings (names of people who have borrowed the book)

# 2️⃣ The function should return a new dictionary with:

# Each book title as the key.

# The value should be another dictionary with:

# 'author': the author’s name

# 'status': a string — "Available" if available_copies > 0, otherwise "Not Available"

# 'borrowed_by': list of names of people who borrowed the book

def library_tracker(book_list: list[dict]) -> dict:
    
    new_dict = {}
    
    for book in book_list:
        title = book.get("title")
        author = book.get("author")
        status = book.get("available_copies")
        borrowed_by = book.get("borrowed")
        
        new_dict[title] = {
            "author" : author,
            "status" : "Available" if status > 0 else "Not available",
            "borrowed_by" : borrowed_by
        }
    return new_dict

books = [
    {
        "title": "Python Basics",
        "author": "John Doe",
        "available_copies": 2,
        "borrowed": ["Alice"]
    },
    {
        "title": "Machine Learning",
        "author": "Jane Smith",
        "available_copies": 0,
        "borrowed": ["Bob", "Charlie"]
    }
]

print(library_tracker(books))
    
    