# -*- coding: utf-8 -*-


def to_rna(dna):
    """Rna Transcription.

    Write a program that, given a DNA strand, returns its RNA complement
    (per RNA transcription).
    :param dna:
    """

    transitions = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }

    # dst = string.translate(sequence, string.maketrans("ATGC","UACG"))
    return ''.join(transitions[nuc] for nuc in dna)

if __name__ == '__main__':
    assert to_rna('GTA') == 'CAU', 'RNA complement for GTA is not CAU'
