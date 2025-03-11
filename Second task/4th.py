# Part 4.............................

# Define the dictionary
book = {}

# Add books with unique ISBNs
book["978-3-16-148410-0"] = ("Treasure Island", "Robert Louis Stevenson", 15.99, {" Fiction ", "Adventure "})
book["978-0-452-28423-4"] = ("Moby-Dick", "Herman Melville", 18.50, {" FICTION", " Adventure"})
book["978-0-7432-7356-5"] = ("The Great Gatsby", "F. Scott Fitzgerald", 10.99, {"Classic ", "FICTION"})
book["978-0-316-76948-0"] = ("Treasure Island", "Robert Louis Stevenson", 12.99, {"FICTION ", "Adventure"})

# Function to standardize genres
def standardize_genres():
    for isbn, details in book.items():
        title, author, price, genres = details  # Extract old details
        cleaned_genres = {genre.strip().lower() for genre in genres}  # Clean genres
        book[isbn] = (title, author, price, cleaned_genres)  # Update book tuple

# Example usage
standardize_genres()
print(book)