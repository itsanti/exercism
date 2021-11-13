def can_chain(dominoes):
    if len(dominoes) < 1:
        return []
    result = []
    dominoes = [[ix, d] for ix, d in enumerate(dominoes)]

    for i in range(len(dominoes)):
        result = add_domino(result, dominoes)

    for chain in result:
        if chain[0][1][0] == chain[-1][1][1] and len(chain) == len(dominoes):
            return [el[1] for el in chain]
    return None


def add_domino(result, dominoes):
    if len(result) == 0:
        result = [[domino] for domino in dominoes]
        for domino in dominoes:
            result.append([[domino[0], domino[1][::-1]]])
        return result
    for domino in dominoes:
        for chain in result:
            if not domino_in_chain(domino, chain):
                if chain[-1][1][1] == domino[1][0]:
                    result.insert(0, chain.copy())
                    chain.append(domino)
                elif chain[-1][1][1] == domino[1][::-1][0]:
                    result.insert(0, chain.copy())
                    chain.append([domino[0], domino[1][::-1]])
    return result


def domino_in_chain(domino, chain):
    for el in chain:
        if el[0] == domino[0]:
            return True
    return False


if __name__ == '__main__':
    #print(can_chain([(1, 2), (2, 3), (3, 1), (2, 4), (2, 4)]))
    print(can_chain([(1, 2), (2, 3), (3, 1), (1, 1), (2, 2), (3, 3)]))
    #print(can_chain([(1, 2), (1, 3), (2, 3)]))
    #print(can_chain([(1, 2), (3, 1), (2, 3)]))
    #print(can_chain([(1, 2), (2, 1), (3, 4), (4, 3)]))
