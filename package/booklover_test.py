import unittest
from booklover import BookLover

class BookLoverTest(unittest.TestCase):
    def test_1_add_book(self):
        '''test if book in list'''
        bl = BookLover('Will', 'will@gmail.com', 'mystery')
        bl.add_book('Harry Potter 1', 7)
        testValue = 'Harry Potter 1' in bl.book_list['book_name'].values.tolist()
        message = 'The book is not in the list!'
        self.assertTrue(testValue, message)
    def test_2_add_book(self):
        '''add book twice'''
        bl = BookLover('Will', 'will@gmail.com', 'mystery')
        bl.add_book('Harry Potter 2', 8)
        bl.add_book('Harry Potter 2', 8)
        testValue = (bl.book_list['book_name'] == 'Harry Potter 2').sum()
        message = 'The book is in twice!'
        self.assertTrue(testValue == 1, message)
    def test_3_has_read(self):
        '''check list for book'''
        bl = BookLover('Will', 'will@gmail.com', 'mystery')
        bl.add_book('Harry Potter 2', 8)
        testBool = bl.has_read('Harry Potter 2')
        message = 'The book is not in the list!'
        self.assertTrue(testBool, message)
    def test_4_has_read(self):
        '''check for book in list'''
        bl = BookLover('Will', 'will@gmail.com', 'mystery')
        bl.add_book('Harry Potter 2', 8)
        testBool = bl.has_read('Harry Potter 4')
        message = 'The book is in the list!'
        self.assertFalse(testBool, message)
    def test_5_num_books_read(self):
        '''Check books read is correct'''
        bl = BookLover('Will', 'will@gmail.com', 'mystery')
        bl.add_book('Harry Potter 2', 8)
        bl.add_book('Harry Potter 3', 8)
        bl.add_book('Harry Potter 4', 8)
        numBooks = bl.num_books_read()
        expected = 3
        message = 'Number of books read is wrong!'
        self.assertEqual(numBooks, expected, message)
    def test_6_fav_books(self):
        bl = BookLover('Will', 'will@gmail.com', 'mystery')
        bl.add_book('Harry Potter 2', 2)
        bl.add_book('Harry Potter 3', 3)
        bl.add_book('Harry Potter 4', 8)
        favs = bl.fav_books()['book_name'].values.tolist()
        expected = ['Harry Potter 4']
        message = 'The favorite list is incorrect!'
        self.assertEqual(favs, expected, message)

if __name__ == '__main__':
    unittest.main(verbosity=3)