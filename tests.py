"""Test for Nautical Tour's Flask app."""

import unittest
from server import app
from flask import session
from model import connect_to_db, db


class NauticalTests(unittest.TestCase):
    """Tests for my nautical site."""


    def setUp(self):
        """Code to run before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app)



    def test_homePage(self):
        """Confirmation that home page loads"""

        result = self.client.get("/")
        print("RESULT")
        print(result)
        self.assertIn(b"Footer Paragra", result.data)
        

    def test_tourPage(self):
        """Confirmation that tour page loads"""

        result = self.client.get("/tours")
        self.assertIn(b"Footer Paragraph", result.data)
        print("RESULT")
        print(result)
    
    def test_login(self):
            """Test login page."""

            result = self.client.post("/login",
                                    data={"email": "lulu@blu.com", "password": "blue"},
                                    follow_redirects=True)
            self.assertIn(b"Tour Information", result.data)

    def test_tours(self):
        """Test departments page."""

        result = self.client.get("/department/fin")
        self.assertIn(b"Phone: 555-1000", result.data)


    



    


if __name__ == "__main__":
    unittest.main()