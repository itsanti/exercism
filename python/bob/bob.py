def response(hey_bob: str):
    hey_bob = hey_bob.strip()
    if hey_bob.endswith('?'):
        if hey_bob.isupper():
            return 'Calm down, I know what I\'m doing!'
        return 'Sure.'
    elif hey_bob.strip() == '':
        return 'Fine. Be that way!'
    elif hey_bob.isupper():
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'
