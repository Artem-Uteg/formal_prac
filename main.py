'''
Даны α и натуральные числа k, l, такие что 0 ≤ l < k. Проверить, содержит ли
язык L слова, чья длина равна l по модулю k.
'''
import math
import sys

ALPHABET = ['a', 'b', 'c', '1', '.', '+', '*']
SYMBOLS = ['a', 'b', 'c']

EMPTY_SYMBOL = '1'
CONCATENATION = '.'
PLUS = '+'
STAR = '*'


def error():
    print("ERROR")
    sys.exit()


class Language:
    regex = str()
    mod = int()
    remain = int()

    def __init__(self):
        pass

    def contains_word(self, regex, mod, remain):
        if remain >= mod or remain <= 0 or mod <= 1:
            error()
        self.regex = regex
        self.mod = mod
        self.remain = remain
        stack = []
        length_stack = 0

        for symbol in self.regex:
            if symbol not in ALPHABET:
                error()

            if symbol in SYMBOLS:           # символ из алфавита
                stack.append({1})
                length_stack += 1

            elif symbol is EMPTY_SYMBOL:    # пустое слово
                stack.append({0})
                length_stack += 1

            elif symbol is PLUS:            # выбор
                if length_stack < 2:
                    error()
                stack[-2] = self.plus(stack[-1], stack[-2])
                stack.pop()
                length_stack -= 1

            elif symbol is STAR:            # звезда клини
                if length_stack == 0:
                    error()
                stack[-1] = self.star(stack[-1])

            elif symbol is CONCATENATION:   # конкатенация
                if length_stack < 2:
                    error()
                stack[-2] = self.concatenation(stack[-1], stack[-2])
                stack.pop()
                length_stack -= 1

        if length_stack != 1:
            error()
        return self.remain in stack[0]

    def plus(self, first_remains_set, second_remains_set):
        return first_remains_set.union(second_remains_set)

    def star(self, remain_set):
        gcd_length = self.mod
        for remain in remain_set:
            if remain != 0:
                gcd_length = math.gcd(gcd_length, remain)

        result = set()
        coefficient = 1
        new = (gcd_length * coefficient) % self.mod

        while not (new in result):

            coefficient += 1
            result.add(new)
            new = (gcd_length * coefficient) % self.mod

        return result

    def concatenation(self, first_remains_set, second_remains_set):
        result = set()

        for first_remain in first_remains_set:
            for second_remain in second_remains_set:
                result.add((first_remain + second_remain) % self.mod)

        return result
