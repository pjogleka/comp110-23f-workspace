"""File to define Fish class."""


class Fish:
    """Fish class."""
    age: int
    
    def __init__(self):
        """Initialize fish."""
        self.age = 0
        return None
    
    def one_day(self):
        """Fish is older."""
        self.age += 1
        return None