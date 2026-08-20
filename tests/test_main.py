import unittest
from src.main import main
from io import StringIO
import sys

class TestMain(unittest.TestCase):
    
    def test_main_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output  # Redirect stdout
        main()
        sys.stdout = sys.__stdout__  # Reset redirect
        output = captured_output.getvalue().strip()
        self.assertIn("Welcome to Project ReadMe!", output)

if __name__ == '__main__':
    unittest.main()