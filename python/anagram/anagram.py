def find_anagrams(word, candidates):
    s_word = sorted(word.lower())
    r = []
    for w in candidates:
        if s_word == sorted(w.lower()) and word.lower() != w.lower():
            r.append(w)
    return r


if __name__ == '__main__':
    candidates = ["BANANA", "Banana", "banana"]
    print(find_anagrams("BANANA", candidates))
