import numpy as np
import pandas as pd

class BookLover():
    def __init__(self, name, email, fg, nb=0, bl= pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fave_genre = fg
        self.num_books = nb
        self.book_list = bl
    def add_book(self, book_name, rating):
        if book_name not in self.book_list['book_name'].values.tolist():
            new_book = pd.DataFrame({
            'book_name': [book_name], 
            'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        else:
            print(f"{book_name} is already in the list, it won't be added!")
    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            return(True)
        else:
            return(False)
    def num_books_read(self):
        return(len(self.book_list))
    def fav_books(self):
        return(self.book_list[self.book_list['book_rating']>3])

if __name__ == '__main__':
    testObj = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    testObj.add_book("War of the Worlds", 4)
    print(testObj.book_list)


