"""File to define Bear class."""


class Bear:
    """Def bear class."""
    age: int
    hunger_score: int

    def __init__(self):
        """Initialize bear."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Changes to hunger and age."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Bear eats."""
        self.hunger_score += num_fish
        return None