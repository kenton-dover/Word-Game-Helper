import itertools
import os
import urllib.request
import sys
import time

# PREWORK
DICTIONARY = os.path.join(sys.path[0], 'words.txt')
dictionary = []
with open(DICTIONARY) as f:
    [dictionary.append(word.strip().lower()) for word in f.read().split()]
dictionary = set(dictionary)


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    combinations = _get_permutations_draw(draw)
    listOfPossibleWords = []
    try:
        while True:
            combination = next(combinations)
            combination = ''.join(combination)
            if combination in listOfPossibleWords:
                continue
            if combination in dictionary:
                listOfPossibleWords.append(combination)
    except StopIteration:
        if listOfPossibleWords:
            return listOfPossibleWords
        else:
            print("There are no combinations made with those letters.")


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    for _ in range(1, len(draw) + 1):
        for subset in itertools.permutations(draw, _):
            yield(subset)


def main():
    draw = input("Please enter each letter without any spaces: ")
    print(get_possible_dict_words(list(draw)))


if __name__ == '__main__':
    main()
