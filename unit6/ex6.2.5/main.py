from file1 import GreetingCard
from file2 import BirthdayCard


def main():
    greeting_card = GreetingCard()
    birthday_card = BirthdayCard(age=22)

    greeting_card.greeting_msg()
    print("-------------------------------------")
    birthday_card.greeting_msg()


if __name__ == "__main__":
    main()
