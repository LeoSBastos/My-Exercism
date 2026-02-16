"""
Phone Number
"""

import re
import string


class PhoneNumber:
    """
    class
    """

    def __init__(self, number):
        """
        initializer
        """


class PhoneNumber:
    def __init__(self, number):
        if any(c.isalpha() for c in number):
            raise ValueError("letters not permitted")
        if any(c in r"!\"#$%&'\*,/:;<=>\?@\[\\\]^_`{\|\}~" for c in number):
            raise ValueError("punctuations not permitted")

        self.raw = re.findall(
            r"[\d]", number
        )  # initailization of only digits in provided 'number' variable.

        # INPUT VALIDATION - less than 10 digits
        if len(self.raw) < 10:
            raise ValueError("incorrect number of digits")
        # INPUT VALIDATION - More than 11 digits
        if len(self.raw) > 11:
            raise ValueError("more than 11 digits")
        # INPUT VALIDATION - First digit of 11 digit number is not 1
        if len(self.raw) == 11 and int(self.raw[0]) != 1:
            raise ValueError("11 digits must start with 1")
        self.exchange = self.raw[-7:]

        # INPUT VALIDATION - First digit of exchange code is a 0
        if int(self.exchange[0]) in [0]:
            raise ValueError("exchange code cannot start with zero")
        self.area_code = "".join(self.raw[-10:-7])

        # INPUT VALIDATION - First digit of exchange code is a 1
        if int(self.exchange[0]) in [1]:
            raise ValueError("exchange code cannot start with one")
        self.area_code = "".join(self.raw[-10:-7])

        # INPUT VALIDATION - First digit of area code is a 1 or a 0
        if int(self.area_code[0]) in [1]:
            raise ValueError("area code cannot start with one")

        # INPUT VALIDATION - First digit of area code is a 1 or a 0
        if int(self.area_code[0]) in [0]:
            raise ValueError("area code cannot start with zero")
        self.number = "".join(self.raw[-10:])

    def pretty(self):
        """Returns an easy to read version of a given phone number.
        - Example: (###)-###-####"""

        p_number = self.number[-10:]
        return f"({p_number[0:3]})-{p_number[3:6]}-{p_number[6:11]}"
