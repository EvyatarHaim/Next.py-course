class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        return self._hunger > 0

    def feed(self):
        self._hunger -= 1

    def talk(self):
        pass

    def special_method(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")

    def special_method(self):
        self.fetch_stick()


class Cat(Animal):
    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")

    def special_method(self):
        self.chase_laser()


class Skunk(Animal):
    def __init__(self, name, hunger, stink_count=6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")

    def special_method(self):
        self.stink()


class Unicorn(Animal):
    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")

    def special_method(self):
        self.sing()


class Dragon(Animal):
    def __init__(self, name, hunger, color="Green"):
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")

    def special_method(self):
        self.breath_fire()


def main():
    dog = Dog("Brownie", 10)
    cat = Cat("Zelda", 3)
    skunk = Skunk("Stinky", 0)
    unicorn = Unicorn("Keith", 7)
    dragon = Dragon("Lizzy", 1450)
    zoo_lst = [dog, cat, skunk, unicorn, dragon]

    dog2 = Dog("Doggo", 80)
    cat2 = Cat("Kitty", 80)
    skunk2 = Skunk("Stinky Jr.", 80)
    unicorn2 = Unicorn("Clair", 80)
    dragon2 = Dragon("McFly", 80)
    zoo_lst += [dog2, cat2, skunk2, unicorn2, dragon2]

    for animal in zoo_lst:
        if animal.is_hungry():
            print(type(animal).__name__ + " " + animal.get_name())
            while animal.is_hungry():
                animal.feed()
        animal.talk()

        animal.special_method()

    print("\n\nZoo: " + Animal.zoo_name)


if __name__ == '__main__':
    main()
