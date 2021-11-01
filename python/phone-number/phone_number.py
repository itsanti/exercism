class PhoneNumber:
    def __init__(self, number):
        self.number = self.set_number(number)
        self.area_code = self.set_area_code(self.number[:3])

    def set_number(self, number):
        number = [d for d in number if d.isdigit()]
        if len(number) > 10:
            if int(number[0]) != 1:
                raise ValueError('11 digits does not start with a 1')
            number = number[1:]
        if int(number[3]) < 2:
            raise ValueError('exchange code must be 2-9')
        return ''.join(number)

    def set_area_code(self, code):
        if int(code[0]) < 2:
            raise ValueError('area_code must be 2-9')
        return code

    def pretty(self):
        return f'({self.area_code})-{self.number[3:6]}-{self.number[-4:]}'


if __name__ == '__main__':
    pn = PhoneNumber('223.456.7890')
    print(pn.number)
