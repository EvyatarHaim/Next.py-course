def stop_iteration():
    i = iter([1, 2, 3])
    next(i)
    next(i)
    next(i)
    next(i)


def zero_division_error():
    a = 5
    b = 0
    c = a / b


def assertion_error():
    x = 24
    y = 3
    assert x < y, "X is bigger than Y"

# def import_error():
#    import sigit


def key_error():
    some_dict = {"some_key": "some_value"}
    print(some_dict["key"])


# def syntax_error():
#    len('Evyatar') = 5


# def indentation_error():
#    if True:
#    print("Hello World!")


def type_error():
    a = '1'
    b = 4
    c = a + b

