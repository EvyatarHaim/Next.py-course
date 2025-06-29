from file1 import GreetingCard


class BirthdayCard(GreetingCard):
    def __init__(self, age):
        super().__init__()
        self._sender_age = age

    def greeting_msg(self):
        super().greeting_msg()
        print(f"Happy Birthday! \nSender age: {self._sender_age}")
