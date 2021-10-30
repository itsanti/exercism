class Luhn:
    def __init__(self, card_num):
        self.card_num: str = card_num.replace(' ', '')

    def valid(self):
        if len(self.card_num) < 2 or not self.card_num.isdigit():
            return False
        card_num = list(map(int, list(self.card_num)))
        for digit in range(len(card_num) - 2, -1, -2):
            card_num[digit] *= 2
            if card_num[digit] > 9:
                card_num[digit] -= 9
        return not sum(card_num) % 10

if __name__ == '__main__':
    Luhn("4539 3195 0343 6467").valid()