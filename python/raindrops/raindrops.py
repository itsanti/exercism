def convert(number):
    if number % 7 == 0 and not number % 15:
        return 'PlingPlangPlong'
    elif not number % 35:
        return 'PlangPlong'
    elif not number % 21:
        return 'PlingPlong'
    elif not number % 15:
        return 'PlingPlang'
    elif not number % 3:
        return 'Pling'
    elif not number % 5:
        return 'Plang'
    elif not number % 7:
        return 'Plong'
    else:
        return str(number)
