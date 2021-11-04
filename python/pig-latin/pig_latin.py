def translate(text):
    vovels = set(['xr', 'yt', 'a', 'e', 'i', 'o', 'u', 'y'])
    result = []
    for word in text.split(' '):
        if word[:1] in vovels or word[:2] in vovels:
            if word[:2] == 'ye':
                word = word[1:] + 'y'
            word += 'ay'
        else:
            if word[1:3] == 'qu':
                word = word[3:] + word[:3]
            elif word[:2] == 'qu':
                word = word[2:] + word[:2]
            else:
                while word[:1] not in vovels:
                    word = word[1:] + word[:1]
            word += 'ay'
        result.append(word)
    return ' '.join(result)


if __name__ == '__main__':
    print(translate("my"))
