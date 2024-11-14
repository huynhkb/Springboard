"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __int__(self, start=0):
        """Create a serial starting with a"""
        self.start = start
        self.current = start
    
    def generate(self):
        """Returns the starting value of the serial with increment of 1"""
        starting = self.current
        self.current += 1
        return starting
        
    
    def __repr__(self):
        """Returns the starting number and current number in the incremented serial"""
        return f"We started with {self.start} and now we're at {self.current}"
    
    def reset(self):
        """Resets the serial to its original starting point"""
        self.current = self.start
      
