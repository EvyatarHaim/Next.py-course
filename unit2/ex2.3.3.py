class Octopus:
    count_animals = 0

    def __init__(self, name="Octavio"):
        self._name = name
        self._age = 10
        Octopus.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


def main():
    oct1 = Octopus("Evyatar")
    oct2 = Octopus()

    print(oct1.get_name())
    print(oct2.get_name())

    oct1.set_name("Alon")
    print(oct1.get_name())

    print(Octopus.count_animals)


if __name__ == '__main__':
    main()
