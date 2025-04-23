target_book = input()
books_reviewed = 0

current_book = input()
while current_book != 'No More Books':

    if current_book == target_book:
        print(f'You checked {books_reviewed} books and found it.')
        break

    books_reviewed += 1
    current_book = input()

else:
    print(f'The book you search is not here!')
    print(f'You checked {books_reviewed} books.')


