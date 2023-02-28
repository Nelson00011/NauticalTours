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


    def test_home_page(self):
        """Confirmation that home page loads"""

        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)    
        self.assertIn(b"Nautical", result.data)
        

    def test_tour_page(self):
        """Confirmation that tour page loads"""

        result = self.client.get("/tours")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"Hawaii", result.data)
        
    
    def test_login(self):
            """Test login page."""

            result = self.client.post("/login",
                                    data={"email": "lulu@blu.com", "password": "blue"},
                                    follow_redirects=True)
            
            self.assertEqual(result.status_code, 200)
            self.assertIn(b"Tour Information", result.data)

    def test_sign_up(self):
           """Test Sign-Up Page."""

           result = self.client.post("/users", data={
                "fname": "Pear", 
                "lname": "Blu", 
                "email": "lime@blu.com", 
                "password": "blue", 
                "phone": "555-555-5555", 
                "birthday": "1990-01-01"
                }, follow_redirects=False)
    
           self.assertEqual(result.status_code, 200)
           self.assertIn(b"Account Login", result.data)
           

    def test_tours(self):
        """Test departments page."""

        result = self.client.get("/tours/1")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"Arctic Winds", result.data)




if __name__ == "__main__":
    unittest.main()