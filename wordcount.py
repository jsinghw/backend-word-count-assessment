#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys


def helper_func(filename):
    with open(filename, 'r') as f:
        word = f.read()
        word = word.replace('\n', ' ').lower().split(' ')
        word_Dictionary = {}
        for i in word:
            if i != '' and i not in word_Dictionary:
                word_Dictionary[i] = 1
            elif i in word_Dictionary:
                word_Dictionary[i] += 1
    return word_Dictionary


def print_words(filename):
    word_Dictionary = helper_func(filename)
    # learned about string formatting here https://www.learnpython.org/en/String_Formatting
    for key in sorted(word_Dictionary.keys()):
        print('%s: %s' % (key, word_Dictionary[key]))


def print_top(filename):
    # understanding to unpack to get it to sort by items https://stackoverflow.com/questions/15583081/sorting-dictionary-values-error-lambda
    # took me forever to figure out how to get this to work with python 3 because of the change in the way items works in python 3
    word_Dict = helper_func(filename)
    for key, value in sorted(list(word_Dict.items()), key=lambda item: item[1], reverse=True)[:20]:
        print("%s: %s" % (key, value))


def main():

    if len(sys.argv) != 3:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
