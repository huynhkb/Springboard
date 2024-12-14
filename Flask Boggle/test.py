from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class BoggleGameTests(TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Test that the homepage loads with the correct session data and HTML."""
        with self.client:
            response = self.client.get('/')
            self.assertIn('board', session)
            self.assertIsNone(session.get('high_score'))
            self.assertIsNone(session.get('times_played'))
            self.assertIn(b'<strong>High Score:', response.data)
            self.assertIn(b'Current Score:', response.data)
            self.assertIn(b'Time Remaining:', response.data)

    def test_check_valid_word(self):
        """Verify word validity by updating the board in the session."""
        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["C", "A", "T", "S", "P"],
                                ["E", "R", "A", "T", "T"],
                                ["N", "I", "C", "A", "M"],
                                ["D", "E", "R", "O", "G"],
                                ["U", "L", "A", "Q", "Z"]]
        response = self.client.get('/check?word=rat')
        self.assertEqual(response.json['result'], 'ok', "Word 'rat' should be valid on the board")


    def test_check_invalid_word(self):
        """Checking if word is valid or not."""
        self.client.get('/')
        response = self.client.get('/check?word=onomatopoeia')
        self.assertEqual(response.json['result'], 'not-on-board')

    def test_check_random_word(self):
        """Check that random word is identified as invalid."""
        self.client.get('/')
        response = self.client.get('/check?word=bonjourmadam')
        self.assertEqual(response.json['result'], 'not-word', "Random word should be flagged as invalid")
