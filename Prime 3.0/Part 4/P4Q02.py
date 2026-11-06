#  Create a class with the following attributes:
"""
• title
• author
• list of reviews
And add methods to:
• add a new review
• count reviews
• display all reviews"""



class Book:

    # Constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []  # Empty list to store reviews

    # Method to add a new review
    def add_review(self, review):
        self.reviews.append(review)
        print("Review added successfully!")

    # Method to count reviews
    def count_reviews(self):
        return len(self.reviews)

    # Method to display all reviews
    def display_reviews(self):
        print("\nBook Title:", self.title)
        print("Author:", self.author)
        print("\nAll Reviews:")

        for review in self.reviews:
            print("-", review)


# Creating an object
book1 = Book("Python Programming", "Guido van Rossum")

# Adding reviews
book1.add_review("Excellent book for beginners.")
book1.add_review("Easy to understand.")
book1.add_review("Very useful for learning Python.")

# Counting reviews
print("\nTotal Reviews:", book1.count_reviews())

# Displaying all reviews
book1.display_reviews()


"""OUTPUT:
Review added successfully!
Review added successfully!
Review added successfully!

Total Reviews: 3

Book Title: Python Programming
Author: Guido van Rossum

All Reviews:
- Excellent book for beginners.
- Easy to understand.
- Very useful for learning Python.
PS D:\Python> """