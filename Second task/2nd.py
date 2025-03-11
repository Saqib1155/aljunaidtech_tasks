# Part 2........................................


book = {}

# Add books with unique ISBNs
book["978-3-16-148410-0"] = ("Treasure Island", "Robert Louis Stevenson", 15.99, {"fiction", "adventure"})
book["978-0-452-28423-4"] = ("Moby-Dick", "Herman Melville", 18.50, {"fiction", "adventure"})
book["978-0-7432-7356-5"] = ("The Great Gatsby", "F. Scott Fitzgerald", 10.99, {"fiction", "classic"})

# Function to search books by author
def search_by_author(author, inventory):
    result = []
    for isbn, details in inventory.items():
        if details[1] == author:  
            result.append((isbn, details[0]))  
    return result

# Example usage
print(search_by_author("Robert Louis Stevenson", book))
print(search_by_author("Herman Melville", book))
print(search_by_author("F. Scott Fitzgerald", book))
