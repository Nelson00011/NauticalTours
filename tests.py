"""Test for Nautical Tour's Flask app."""

import unittest
from server import app
from flask import session
from model import connect_to_db, db


class NauticalTests(unittest.TestCase):
    """Tests for my nautical site"""


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
        
    def test_about(self):
        """Confirmation that about loads"""

        result = self.client.get("/about")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"<!-- Sendgrid (Twilio) form-->", result.data)
    
    def test_login(self):
            """Test login page"""

            result = self.client.post("/login",
                                    data={"email": "lulu@blu.com", "password": "blue"},
                                    follow_redirects=True)
            
            self.assertEqual(result.status_code, 200)
            self.assertIn(b"Tour Information", result.data)


    def test_sign_up(self):
           """Test Sign-Up Page"""

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

    def test_logout(self):
        """Test Log out functions"""
        result = self.client.post('/logout')
        self.assertEqual(result.status_code, 302)
        self.assertIn(b"Redirecting", result.data)

    def test_tours(self):
        """Test departments page"""

        result = self.client.get("/tours/1")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"Arctic Winds", result.data)

    def test_profile_page(self):
            """Test profile page"""

            result = self.client.post("/login",
                                    data={"email": "lulu@blu.com", "password": "blue"},
                                    follow_redirects=True)
            
            self.assertEqual(result.status_code, 200)        
            self.assertIn(b"Balance", result.data)
            self.assertIn(b"Phone", result.data)

    def test_review_form(self):
        """Test Review Form"""
        with self.client as current:
            with current.session_transaction() as period:
                period['primary_key'] = 3
                period['tour_id']=4
                period['dates']='2019-06-29'
                
        result =self.client.post('/review_submission',
                                 data={                                
                                "star": "5",
                                "comments": "Super excited to see the all the Whales on the second day! Incredible glacial Views! Great crew.",
                                })
        self.assertEqual(result.status_code, 200)        
        self.assertIn(b"Balance", result.data)
                                

    def test_review_page(self):
        """Test Review Page"""
        result = self.client.get('/review/1')
        self.assertEqual(result.status_code, 200)        
        self.assertIn(b'Overall experience (rating)', result.data)
    
    def test_google_map(self):
         """Test Google Map Api call will be correct"""
        
         result = self.client.get("/tours/1")
         self.assertEqual(result.status_code, 200)
         self.assertIn(b'<div id="map" class="alaska">', result.data)





if __name__ == "__main__":
    unittest.main()
