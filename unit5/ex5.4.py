from functools import reduce


class IDIterator:
    """
        Iterator that generates valid ID numbers starting from a given ID
    """
    def __init__(self, id):
        self._id = id

    def __iter__(self):
        return self

    def __next__(self):
        num = self._id + 1
        while num <= 999999999:
            if check_id_valid(num):
                self._id = num
                return num
            num += 1

        raise StopIteration


def check_id_valid(id_number):
    """
       Check if the ID number is valid using the rules (steps)
       :param id_number: ID number to check
       :type id_number: int
       :return: True if valid, False otherwise
       :rtype: bool
   """
    numbers_list = [int(i) for i in str(id_number)]
    mul_list = [num * 1 if index % 2 != 0 else num * 2 for index, num in enumerate(numbers_list)]
    before_sum_list = [num % 10 + num if num > 9 else num for num in mul_list]
    sum_of_list = reduce(lambda num1, num2: num1 + num2, before_sum_list)

    return sum_of_list % 10 == 0


def id_generator(id_number):
    """
        Generator that yields valid ID numbers starting after the given ID
        :param id_number: starting ID number
        :type id_number: int
        :yield: next valid ID number
        :rtype: int
    """
    new_id = id_number + 1
    while new_id <= 999999999:
        if check_id_valid(new_id):
            yield new_id
        new_id += 1


def main():
    # Check for valid input
    while True:
        user_input = input("Enter ID (9 digits): ")
        if len(user_input) == 9 and user_input.isdigit():
            user_id = int(user_input)
            break
        else:
            print("Invalid input. Please enter exactly 9 digits.")

    iter_gen = input("Generator or Iterator? (gen/it)? ")
    if iter_gen == "it":
        iterator = iter(IDIterator(user_id))
        for i in range(10):
            new_id = next(iterator)
            print(new_id)
    else:
        generator = id_generator(user_id)
        for i in range(10):
            new_id = next(generator)
            print(new_id)


if __name__ == '__main__':
    main()
