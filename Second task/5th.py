# Part 5............................

book = {}

book["978-3-16-148410-0"] = ("Treasure Island", "Robert Louis Stevenson", 15.99, {"fiction", "adventure"})
book["978-0-452-28423-4"] = ("Moby-Dick", "Herman Melville", 18.50, {"fiction", "adventure"})
book["978-0-7432-7356-5"] = ("The Great Gatsby", "F. Scott Fitzgerald", 10.99, {"classic", "fiction"})
book["978-0-316-76948-0"] = ("Treasure Island", "Robert Louis Stevenson", 12.99, {"fiction", "adventure"})

def display_inventory():
    print(f"{'ISBN':<20} {'Title':<25} {'Author':<25} {'Price':<10} {'Genres'}")
    print("-" * 90)  
    
    for isbn, details in book.items():
        title, author, price, genres = details
        genres_str = ", ".join(genres) 
        print(f"{isbn:<20} {title:<25} {author:<25} ${price:<10.2f} {genres_str}")

display_inventory()
