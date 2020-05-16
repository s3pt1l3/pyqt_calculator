import operator

OPERATORS = {'+': (1, operator.add), '-': (1, operator.sub),
             '×': (2, operator.mul), '÷': (2, operator.truediv)}


def reverse_polish_notation(st):
    def parse(st):
        number = ''
        for s in st:
            if s in '1234567890.':
                number += s
            elif number:
                yield float(number)
                number = ''
            if s in OPERATORS or s in "()":
                yield s
        if number:
            if number.count('.') > 1:
                yield 'ERROR: TWO DOTS IN ONE NUMBER'
            else:
                yield float(number)

    def shunting_yard(parsed_st):
        if parsed_st == 'ERROR: TWO DOTS IN ONE NUMBER':
            yield 'ERROR: TWO DOTS IN ONE NUMBER'
        stack = []
        for token in parsed_st:
            if token in OPERATORS:
                while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                stack.append(token)
            else:
                yield token
        while stack:
            yield stack.pop()

    def calc(p_st):
        if p_st == 'ERROR: TWO DOTS IN ONE NUMBER':
            return 'ERROR: TWO DOTS IN ONE NUMBER'
        else:
            stack = []
            for token in p_st:
                if token in OPERATORS:
                    y, x = stack.pop(), stack.pop()
                    if token == '÷' and y == 0:
                        return 'ERROR: DIVISION BY ZERO'
                    else:
                        stack.append(OPERATORS[token][1](x, y))
                else:
                    stack.append(token)
            if str(stack[0])[-1] == '0':
                stack[0] = int(stack[0])
            return stack[0]

    return calc(shunting_yard(parse(st)))
