def abbreviate(words: list[str]):
    return ''.join([word.capitalize()[0] for word in ' '.join(words.replace('_','').split('-')).split()])
