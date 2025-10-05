class Muffin:
    cook_levels=["underdone","well done", "overdone"]
    def __init__(self, flavor, price): 
        self.flavor = flavor
        self.price = price
        self.current_level = 0  # Start as underdone
    def __str__(self):
        return self.flavor
    def bake_muffin(self):
        if self.current_level < len(Muffin.cook_levels) - 1: # Prevent going out of bounds
            self.current_level += 1 # Increment cooking level
    def get_description(self):
        return f"{Muffin.cook_levels[self.current_level]} {self.flavor} muffin priced at ${self.price:.2f}" # Formatted price