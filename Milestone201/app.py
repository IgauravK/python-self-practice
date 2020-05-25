import utils.database

user_choice = '''
Please enter:
- 'A' to add a new book
- 'L' to list all books
- 'R' to mark a book as read
- 'D' to delete a book
- 'Q' to quit the app
Your choice: '''


user_options = {
        "A": utils.database.add_book,
        "L": utils.database.list_books,
        "R": utils.database.read_book,
        "D": utils.database.delete_book
    }

def menu():
    user_input = input(user_choice)
    while user_input != 'Q':
        if user_input in user_options:
            selected_function = user_options[user_input]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        user_input = input(user_choice)

menu()


