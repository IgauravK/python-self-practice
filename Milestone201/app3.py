import utils1.database2


user_choice = '''
Please enter:
- 'A' to add a new book
- 'L' to list all books
- 'R' to mark a book as read
- 'D' to delete a book
- 'Q' to quit the app
Your choice: '''


def prompt_add_book():
    name = input('Enter the book name: ')
    author = input('Enter the author name: ')
    utils1.database2.add_book(name,author)


def list_books():
    books = utils1.database2.get_all_books()
    for book in books:
        read = "Yes" if book['read'] else "No"
        print(f"Title: {book['name']} by Author: {book['author']}, read: {read}")


def prompt_read_book():
    name = input('Enter the name of book you want to mark as read: ')
    utils1.database2.mark_book_as_read(name)


def prompt_delete_book():
    name = input('Enter the name of book you want to delete: ')
    utils1.database2.delete_book(name)


def menu():
    utils1.database2.create_book_table()
    user_input = input(user_choice)
    while user_input != 'Q':
        if user_input == 'A':
            prompt_add_book()
        elif user_input == 'L':
            list_books()
        elif user_input == 'R':
            prompt_read_book()
        elif user_input == 'D':
            prompt_delete_book()
        else:
            print('Unknown command. Please try again.')

        user_input = input(user_choice)

menu()
