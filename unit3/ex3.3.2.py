class UnderAge(Exception):
    def __init__(self, age):
        self._age = age

    def __str__(self):
        return f"Your are under 18. You are only {self._age} years old! \nYou can come to Ido's birthday party " \
               f"in {18 - self._age} years!"


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age=age)
    except UnderAge as e:
        print(e)
    else:
        print("You should send an invite to " + name)


send_invitation("Evyatar", 17)
send_invitation("Alon", 20)
