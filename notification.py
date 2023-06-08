class Notification:
    def __init__(self, message):
        self.message = message
        self.is_sent = False

notification_one = Notification('Hello, world!')
print(notification_one.message)
notification_one.is_sent = True
notification_two = Notification('Goodbye!')

print(f'Notification One has been sent: {notification_one.is_sent}')
print(f'Notification Two has been sent: {notification_two.is_sent}')