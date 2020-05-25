from typing import List, Dict, Union

from .database_connection import DatabaseConnection

Books = Dict[str, Union[str,int]]

def create_book_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('Create table if not exists books(Name text primary key, Author text, Read integar)')


def add_book(name: str,author: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        #cursor.execute(f'Insert into Books values ("{name}", "{author}", 0)')
        cursor.execute('Insert into books values (?,?,0)', (name, author))


def get_all_books() -> List[Books]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('select * from books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    return books


def mark_book_as_read(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('Update books set  read=1 where name=?', (name,))


def delete_book(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('Delete from books where name=?', (name,))

