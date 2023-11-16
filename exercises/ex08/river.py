"""File to define River class."""

__author__ = '730569615'

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """River class."""
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check ages."""
        surviving_bears: list[Bear] = self.bears
        surviving_fish: list[Fish] = self.fish
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.bears = surviving_bears
        self.fish = surviving_fish
        return None
    
    def remove_fish(self, amount: int):
        """Removes fish."""
        self.fish = self.fish[amount:]
        return None

    def bears_eating(self):
        """Bears eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Check hunger."""
        surviving_bears: list[Bear] = self.bears
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None
        
    def repopulate_fish(self):
        """Repopulate fish."""
        pairs = len(self.fish) // 2
        for i in range(pairs * 4):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Repopulate bears."""
        pairs = len(self.bears) // 2
        for i in range(pairs):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Prints river stats."""
        print(f'~~~ Day {self.day}: ~~~')
        print(f'Fish population: {len(self.fish)}')
        print(f'Bear population: {len(self.bears)}')
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        for i in range(7):
            self.one_river_day()
