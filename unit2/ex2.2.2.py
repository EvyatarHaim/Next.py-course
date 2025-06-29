class Octopus:
    def __init__(self):
        self.name = "Octavio"
        self.age = 10

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


def main():
    oct1 = Octopus()
    oct2 = Octopus()
    oct1.birthday()

    print(oct1.get_age())
    print(oct2.get_age())


if __name__ == '__main__':
    main()
    