import re

class PhoneNumber:
    def __init__(self, number):
        if len(number) < 10:
            raise ValueError("Number Invalid")
        self.number = "".join(re.findall(r'\d+', number))
        if(len(self.number) > 10 and self.number[0]=="1"):
            self.number = self.number[1:11]
        if len(self.number) > 10:
            raise ValueError("Number Invalid")
        if(self.number[3] == "0" or self.number[3]=="1"):
            raise ValueError("Number Invalid")
        self.area_code = self.number[0:3]
        if self.area_code[0] == "1" or self.area_code[0] == "0":
            raise ValueError("Number Invalid")

    def pretty(self):
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:10]}"