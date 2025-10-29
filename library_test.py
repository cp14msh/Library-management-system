import unittest
from library import Library


class Test_library(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_new_book(self):

        self.library.add_book("1984", "George Orwell")

        self.assertEqual(len(self.library.book), 1)
        self.assertEqual(self.library.book[0]["title"], "1984")
        self.assertEqual(self.library.book[0]["author"], "George Orwell")

    def test_remove_existing_book(self):

        self.library.add_book("1984", "George Orwell")
        self.library.add_book("Animal Farm", "George Orwell")

        self.library.remove_book("1984")

        self.assertEqual(len(self.library.book), 1)
        self.assertEqual(self.library.book[0]["title"], "Animal Farm")

    
if __name__ == "__main__":
    unittest.main()
