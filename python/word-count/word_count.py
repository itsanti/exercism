import re


def count_words(sentence):
    words = {}
    sentence = re.sub(r'[\n\t,_!.&@$%^&: ]+|\'{2,}', '_', sentence)
    for word in sentence.split('_'):
        if word:
            word = word.strip("'").lower()
            words[word] = words.get(word, 0) + 1
    return words
