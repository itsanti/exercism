def answer(question):
    parts = question.split()
    expression = []
    operations = {
        'plus': '+', 'minus': '-', 'multiplied': '*', 'divided': '/'
    }
    for part in parts:
        if part.isdecimal():
            expression.append(part)
        elif part[-1] == '?':
            try:
                expression.append(str(int(part[:-1])))
            except ValueError:
                if part[:-1] not in operations.keys():
                    if len(expression) == 0 and question == 'What is?':
                        raise ValueError("syntax error")
                    raise ValueError("unknown operation")
                else:
                    expression.append(part[:-1])
        elif part in operations.keys():
            expression.append(part)
        elif part[0] == '-':
            expression.append(part)

    if len(expression) == 1:
        if expression[0] not in operations.keys():
            return int(expression[0])
        else:
            raise ValueError("syntax error")

    valid_mask = [part not in operations.keys() for part in expression]

    if not valid_mask[0] or not valid_mask[-1]:
        raise ValueError("syntax error")

    if len(valid_mask) % 2 == 0:
        if expression[-2] == 'multiplied':
            raise ValueError("unknown operation")
        if not valid_mask[1] and not valid_mask[2]:
            raise ValueError("syntax error")
        if valid_mask[-2] and valid_mask[-1]:
            raise ValueError("syntax error")
        raise ValueError("unknown operation")

    if valid_mask[1]:
        raise ValueError("syntax error")

    result = 0
    op = ''
    for part in expression:
        if part in operations.keys():
            op = part
        else:
            if op:
                result = int(eval(f'{result}{operations[op]}{part}'))
                op = ''
            else:
                result += int(part)
    return result


if __name__ == '__main__':
    print(answer("What is 7 plus multiplied by -2?"))
    #print(answer("What is 1 plus 2 1?"))
    #print(answer("What is 7 plus multiplied by -2?"))
    #print(answer('What is 52?'))
    #print(answer('What is -3 plus 7 multiplied by -2?'))
    #print(answer('What is 52 cubed?'))
    #print(answer('What is 25 divided by 5?'))
    #print(answer('What is 3 plus 2 multiplied by 3?'))

