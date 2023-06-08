class MovingThing:
    def __init__(self, x_position, y_position, x_velocity, y_velocity):
        self.x_position = x_position
        self.y_position = y_position
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def update_position(self, time):
        self.x_position += self.x_velocity * time
        self.y_position += self.y_velocity * time

moving_thing = MovingThing(0, 10, 3, 1)
print(f'Original position: ({moving_thing.x_position}, {moving_thing.y_position})')

moving_thing.update_position(2)
print(f'Position after one update: ({moving_thing.x_position}, {moving_thing.y_position})')

moving_thing.update_position(4)
moving_thing.update_position(5)
print(f'Position after two more updates: ({moving_thing.x_position}, {moving_thing.y_position})')