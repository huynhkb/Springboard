"""Word Finder: finds random words from a dictionary."""
from random import choice # importing a method from a library

class WordFinder():
    def __init__(self, filename):
        """Initialize with the name of the file"""
        self.filename = filename
    
    def __repr__(self):
        """Return a random word from the instance method read_file"""
        return self.read_file()
    
    def read_file(self):
        """Read the content and return as a string"""
        file = open(self.filename, 'r')
        try:
            dictionary = file.read().splitlines()
            return choice(dictionary)
        finally:                         # Closing the file
            file.close() 
