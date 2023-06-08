class Dog:
    def __init__(self, name):
        self.name = name

rover = Dog('Rover')
spot = Dog('Spot')
print(f"First dog: {rover.name}")
print(f"Second dog: {spot.name}")