class BigThing:
    def __init__(self, var):
        self._var = var

    def size(self):
        if isinstance(self._var, (int, float)):
            return self._var
        else:
            return len(self._var)


class BigCat(BigThing):
    def __init__(self, var, weight):
        super().__init__(var)
        self._weight = weight

    def size(self):
        if self._weight > 20:
            return "Very Fat"
        elif self._weight > 15:
            return "Fat"
        else:
            return "OK"


def main():
    my_thing = BigThing("balloon")
    print(my_thing.size())
    cutie = BigCat("mitzy", 22)
    print(cutie.size())


if __name__ == '__main__':
    main()
