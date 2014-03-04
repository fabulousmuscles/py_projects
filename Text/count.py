#!/usr/bin/env python

##Count Words in a String##
# Counts the number of individual words in a string and displays
# the top 5 most used words.

import string
from collections import Counter

MY_PROMPT = lambda: raw_input("> ")


def main(prompt):
    print "Welcome."
    print "Enter some words and I'll count them for you."
    print "I'll also tell you the top 5 most used words."
    phrase = prompt()
    while not phrase:
        print "I couldn't detect any words.. Please try again."
        phrase = prompt()
    words = string.translate(
        phrase.strip(), None, string.punctuation
    ).split(' ')
    count = Counter()
    for word in words:
        count[word.lower()] += 1
    num_words = len(words)
    print "There were a total of %d words counted." % num_words
    if num_words < 5:
        print "The %d most used words were:" % num_words
    else:
        print "The 5 most used words were:"
    print count.most_common(5)

if __name__ == "__main__":
    main(MY_PROMPT)
