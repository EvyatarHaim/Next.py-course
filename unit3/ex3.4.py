import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username):
        self._username = username
        self._illegal_char = ''
        self._index = None
        # Call the function when the exception is raised
        self.check_index()

    def check_index(self):
        index = 0
        for char in self._username:
            if not (char.isalnum() or char == "_"):
                self._illegal_char = char
                self._index = index
            index += 1

    def __str__(self):
        return f"This username contains an illegal character \'{self._illegal_char}\' at index {self._index}"


class UsernameTooShort(Exception):
    def __str__(self):
        return "This username contains less than 3 characters"


class UsernameTooLong(Exception):
    def __str__(self):
        return "This username contains more than 16 characters"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "This password does not contain each one of the required characters - "


class PasswordTooShort(Exception):
    def __str__(self):
        return "This password contains less than 8 characters"


class PasswordTooLong(Exception):
    def __str__(self):
        return "This password contains more than 40 characters"


# Subclasses of PasswordMissingCharacter
class MissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Upper)"


class MissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Lower)"


class MissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Digit)"


class MissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return  super().__str__() + "(Special)"


def check_input(username, password):
    try:
        # Check the username
        if not is_valid_username_chars(username):
            raise UsernameContainsIllegalCharacter(username=username)
        elif len(username) < 3:
            raise UsernameTooShort
        elif len(username) > 16:
            raise UsernameTooLong

        # Check the password
        if not any(char.isupper() for char in password):
            raise MissingUppercase
        elif not any(char.islower() for char in password):
            raise MissingLowercase
        elif not any(char.isdigit() for char in password):
            raise MissingDigit
        elif not any(char in string.punctuation for char in password):
            raise MissingSpecial
        elif len(password) < 8:
            raise PasswordTooShort
        elif len(password) > 40:
            raise PasswordTooLong

    except Exception as e:
        print(e)

    else:
        print("OK")


# Check if the username contain illegal character, if so return False (is_valid)
def is_valid_username_chars(username):
    for char in username:
        if not (char.isalnum() or char == "_"):
            return False
    return True


def main():
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")


if __name__ == '__main__':
    main()
