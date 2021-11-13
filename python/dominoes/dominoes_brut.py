def can_chain(dominoes):
    if len(dominoes) < 1:
        return []
    if len(dominoes) < 2:
        if dominoes[0][0] == dominoes[0][1]:
            return dominoes
        else:
            return None
    for chain in can_chain_all(dominoes):
        if chain[0][0] == chain[-1][1]:
            return chain
    return None


def can_chain_all(dominoes):
    if len(dominoes) < 2:
        return [dominoes]
    result = []
    for ix, elem in enumerate(dominoes):
        doms = dominoes.copy()
        doms.pop(ix)
        for chain in can_chain_all(doms):
            if _test_chain(chain):
                if elem[1] == chain[0][0]:
                    result.append([elem] + chain)
                elif elem[::-1][1] == chain[0][0]:
                    result.append([elem[::-1]] + chain)
                elif elem[0] == chain[-1][1]:
                    result.append(chain + [elem])
                elif elem[::-1][0] == chain[-1][1]:
                    result.append(chain + [elem[::-1]])
    return result


def _test_chain(chain):
    if len(chain) < 2:
        return True
    for ix, el in enumerate(chain[:-1]):
        if el[1] != chain[ix + 1][0]:
            return False
    return True


if __name__ == '__main__':
    print(can_chain([(4, 1), (1, 2), (2, 3)]))
    #print(can_chain([(1, 2), (3, 1)]), sep='\n')
    #print(can_chain([(1, 2), (3, 1), (2, 3)]), sep='\n')
    #print(can_chain([(1, 2), (2, 3), (3, 1), (2, 4), (2, 4)]), sep='\n')

