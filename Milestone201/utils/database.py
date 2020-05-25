Books = []

def add_book():
    name = input('Enter the book name: ')
    author = input('Enter the author name: ')
    #read = input('Enter true or false: ')

    Books.append({
        'Name' : name,
        'Author' : author,
        'Read' : False
    })

def list_books():
    for book in Books:
        print_book(book)

def print_book(book):
    read = "Yes" if book['Read'] else "No"
    print(f"Title: {book['Name']} by Author: {book['Author']}, read: {read}")
    #print(f"Author: {book['Author']}")
    #print(f"Read: {book['Read']}")

def read_book():
    read_book_name = input('Enter the name of book you want to mark as read: ')
    for book in Books:
        if book['Name'] == read_book_name:
            book['Read'] = True

def delete_book():
    name = input('Enter the name of book you want to delete: ')
    global Books
    Books = [book for book in Books if book['Name'] != name]









