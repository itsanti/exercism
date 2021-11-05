
def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")

    bests = [[]] + [-1] * (target + max(coins))

    for i in range(target):
        if bests[i] == -1:
            continue
        for c in coins:
            cs = bests[i] + [c]
            if bests[c + i] == -1 or len(cs) < len(bests[c + i]):
                bests[c + i] = sorted(cs)

    if bests[target] == -1:
        raise ValueError("can't make target with given coins")

    return bests[target]


if __name__ == '__main__':
    #print(find_fewest_coins([1], 3))
    #print(find_fewest_coins([4, 5], 27))  # [4, 4, 4, 5, 5, 5]
    print(find_fewest_coins([1, 4, 15, 20, 50], 23))  # [4, 4, 15]
    #print(find_fewest_coins([5, 10], 94))