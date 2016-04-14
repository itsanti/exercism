# -*- coding: utf-8 -*-

import string

def is_pangram(sentence):
    """Determines if a sentence is a pangram.

    A pangram is a sentence that contains at least one occurrence of every letter in the alphabet.
    Returns True if a given sentence is a pangram.
    """
    return set(string.ascii_lowercase).issubset(set(sentence.lower()))
