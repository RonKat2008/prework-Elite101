from items import stock
import unittest
from main import item_return, item_exchange, remove_item

#Run tests on the 3 functions that mainly handle the stock dictionary to test for TypeError which would be the error that would appear!
class TestChatBot(unittest.TestCase):
    def test_item_return(self):
        # Test invalid input types for item_return
        with self.assertRaises(TypeError):
            item_return(12, stock)  # Passing an integer
        with self.assertRaises(TypeError):
            item_return(False, stock)  # Passing a boolean
        with self.assertRaises(TypeError):
            item_return(1.09, stock)  # Passing a float
        with self.assertRaises(TypeError):
            item_return({"id",1}, stock)  # Passing a dictionary
    
    def test_item_exchange(self):
        # Test invalid input types for item_exchange
        with self.assertRaises(TypeError):
            item_exchange('asdfadsf', stock)  # Passing a string
        with self.assertRaises(TypeError):
            item_exchange([1, 2], stock)  # Passing a list
        with self.assertRaises(TypeError):
            item_exchange(50, stock) # Passing an integer
        with self.assertRaises(TypeError):
            item_exchange({"id",1}, stock)  # Passing a dictionary

    def test_remove_item(self):
        # Test invalid input types for remove_item
        with self.assertRaises(TypeError):
            remove_item(True, stock)  # Passing a boolean
        with self.assertRaises(TypeError):
            remove_item(12, stock)  # Passing an integer
        with self.assertRaises(TypeError):
            remove_item('asdfasf', stock)# Passing a string
        with self.assertRaises(TypeError):
            remove_item({"id",1}, stock)  # Passing a dictionary

# Run the tests
if __name__ == "__main__":
    unittest.main()
