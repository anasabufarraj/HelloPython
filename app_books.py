#!./venv/bin/python3.7
# Copyright 2019. Anas Abu Farraj
"""Book store app.

[x]: Add books with book name and author to database.
[x]: Show all books in the database.
[x]: Mark a book as 'read'.
[x]: Remove a book from the list
[x]: Quit the program
"""
from utils import database_json as database

USER_CHOICE = """
Enter:
➤ 'a' or 'add' to add a new book
➤ 'l' or 'list' to list all books
➤ 'm' or 'mark' to mark a book as read
➤ 'd' or 'delete' to delete a book
➤ 'q' or 'quit' to quit

Enter your choice and press ENTER: """


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q' and user_input != 'quit':
        if user_input == 'a' or user_input == 'add':
            add_book()
        elif user_input == 'l' or user_input == 'list':
            list_books()
        elif user_input == 'm' or user_input == 'mark':
            mark_as_read()
        elif user_input == 'd' or user_input == 'delete':
            delete_book()
        else:
            print('Unknown option. Please try again: ')

        user_input = input('\nEnter your choice and press ENTER: ')


def add_book():
    """Ask for book name and author and add to database."""
    name = input('New Book name: ')
    author = input('Enter Author\'s name: ')
    database.add_book(name, author)


def list_books():
    """Show all books in the database."""
    books = database.get_all_books()
    for n, book in enumerate(books, 1):
        read = 'yes' if book['read'] else 'no'
        print(
            f"{[n]} - {book['name'].capitalize()} by {book['author'].capitalize()} — Read: {read}"
        )


def mark_as_read():
    """Ask for book name and mark as 'read' in database."""
    name = input('Enter the name of finish reading book: ')
    database.change_to_read(name)


def delete_book():
    """Ask for book name and remove it from the database."""
    name = input('Enter book name to delete: ')
    database.remove_book(name)


menu()
