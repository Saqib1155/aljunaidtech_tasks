# Part 6....................................

book = {}

book["978-3-16-148410-0"] = ("Treasure Island", "Robert Louis Stevenson", 15.99, {"fiction", "adventure"})
book["978-0-452-28423-4"] = ("Moby-Dick", "Herman Melville", 18.50, {"fiction", "adventure"})
book["978-0-7432-7356-5"] = ("The Great Gatsby", "F. Scott Fitzgerald", 10.99, {"classic", "fiction"})
book["978-0-316-76948-0"] = ("Treasure Island", "Robert Louis Stevenson", 12.99, {"fiction", "adventure"})

def list_all_books():
    titles = {details[0] for details in book.values()} 
    return sorted(titles) 

sorted_titles = list_all_books()
print(sorted_titles)
