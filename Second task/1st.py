
#First task........................................


# Second task........................................

book ={}

 book["978-3-16-148410-0"]= ("Treasure Island", "Robert Louis Stevenson", 15.99, {"fiction", "adventure"}),
 book["978-3-16-148410-0"]= ("Moby-Dick", "Herman Melville", 18.50, {"fiction", "adventure"}),
 book["978-0-7432-7356-5"]= ("The Great Gatsby", "F. Scott Fitzgerald", 10.99, {"fiction", "classic"}),
 book["978-0-316-76948-0"]= ("Treasure Island", "Robert Louis Stevenson", 12.99, {"fiction", "adventure"})


def search_by_author(author, inventory):
    result = []
    for isbn, details in inventory.items():
        if details[1] == author:  
            result.append((isbn, details[0]))  
    return result


