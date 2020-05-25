from app import books

USER_CHOICE = '''Enter one of the following
- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalogue
- 'q' to exit
Enter your choice: '''




def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price) [:10]
    for book in cheapest_books:
        print (book)

print_cheapest_books()

def print_bestcheapest_books():
    bestcheapest_books = sorted(books, key=lambda x: (x.rating*-1, x.price)) [:10]
    for book in bestcheapest_books:
        print (book)

print_bestcheapest_books()

def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating*-1) [:10]
    for book in best_books:
        print (book)

print_best_books()