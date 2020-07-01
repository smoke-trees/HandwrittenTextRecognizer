
'''
# From PySpellChecker
from spellchecker import SpellChecker

spell = SpellChecker()


def correct_sentence(line):
    lines = line.strip().split(' ')
    new_line = ""
    similar_word = {}
    for l in lines:
        new_line += spell.correction(l) + " "
    # similar_word[l]=spell.candidates(l)
    return new_line

'''

from autocorrect import Speller

def correct_sentence(line):   
    spell = Speller()
    return spell(line)

def main():
    print(correct_sentence('Therlftad n th herdisepie'))

if  __name__ == "__main__":
    main()