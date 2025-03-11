#Part 3.........................

# Define the dictionary
book = {}

# Add books with unique ISBNs
book["978-3-16-148410-0"] = ("Treasure Island", "Robert Louis Stevenson", 15.99, {"fiction", "adventure"})
book["978-0-452-28423-4"] = ("Moby-Dick", "Herman Melville", 18.50, {"fiction", "adventure"})
book["978-0-7432-7356-5"] = ("The Great Gatsby", "F. Scott Fitzgerald", 10.99, {"fiction", "classic"})
book["978-0-316-76948-0"] = ("Treasure Island", "Robert Louis Stevenson", 12.99, {"fiction", "adventure"})

# Function to update book price
def update_price(isbn, new_price):
    if isbn in book:  # Check if ISBN exists
        title, author, _, genres = book[isbn]  # Extract old details
        book[isbn] = (title, author, new_price, genres)  # Replace with new tuple
        print(f"Price updated for ISBN {isbn}: New Price ${new_price}")
    else:
        print("ISBN not found.")

# Example usage
update_price("978-3-16-148410-0", 34.99)
print(book)
