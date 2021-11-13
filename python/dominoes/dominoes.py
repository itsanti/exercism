"""
Dominoes
https://exercism.org/tracks/python/exercises/dominoes

"""
from typing import Iterable, List
from random import shuffle


def can_chain(dominoes: Iterable[tuple]) -> List[tuple]:
    """Chain dominoes together or flag as not valid

    :param dominoes: Iterable[tuple] - input list of dominoes represented as tuples
    :return: List[tuple] - chain of dominoes
    """
    if not dominoes:
        return []
    # Brute-force the chain creation by shuffling the dominoes and
    #  attempting to create chain. Return first successful chain.
    # Ugly, but it is faster than using permutations since problematic
    #  overs are quickly jumped over
    for _ in range(42):
        chain = brute_force(dominoes)
        if chain and len(chain) == len(dominoes) and chain[0][0] == chain[-1][1]:
            return chain
    else:
        return None


def brute_force(dominoes: Iterable[tuple]) -> List[tuple]:
    working_set = list(dominoes)
    shuffle(working_set)
    chain = [working_set.pop()]
    while working_set:
        for domino in working_set:
            if domino[0] == chain[-1][1]:
                chain.append(domino)
                working_set.remove(domino)
                break
            elif domino[1] == chain[-1][1]:
                chain.append(domino[::-1])
                working_set.remove(domino)
                break
        else:
            return []
    return chain
