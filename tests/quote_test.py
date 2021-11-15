import unittest
from app.models import Quote


class QuoteTest(unittest.TestCase):
    def setUp(self):
        """Will run before every test"""
        self.new_quote = Quote(1,"Chelsea","Of importance is life.")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))

    
if __name__ == '__main__':
    unittest.main()