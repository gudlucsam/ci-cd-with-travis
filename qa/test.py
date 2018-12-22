import unittest
import pandas as pd
from .app import app
from .parsedata import convert_to_list

class TestAskMe(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
    
    def tearDown(self):
        pass

    def test_page(self):
        response = self.app.get('/askme', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_num_docs(self):
        self.assertEqual(len(convert_to_list("qa/dataset/Answers.txt")), 2609)

if __name__ == "__main__":
    unittest.main()
