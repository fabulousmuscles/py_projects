#!/usr/bin/env python

##Count Words in a String##
# Counts the number of individual words in a string or file and displays
# (up to) the top 10 most used words.

import string
import re
from collections import Counter

MY_PROMPT = lambda: raw_input("> ")


def file_mode(prompt):
    print "Enter a filename and I'll count the words in that file."
    filename = prompt()
    while not filename:
        print "I couldn't detect a filename.. Please try again."
        filename = prompt()
    try:
        words = re.findall(r'\w+', open(filename).read().lower())
    except IOError:
        print "Couldn't find the file! Please try again with a valid filename."
        exit(1)
    count = Counter()
    for word in words:
        count[word] += 1
    num_words = len(words)
    return count, num_words


def phrase_mode(prompt):
    print "Enter some words and I'll count them for you."
    print "I'll also tell you the top 10 most used words."
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
    return count, num_words


def get_input(prompt):
    print "Would you like me to count the words in a phrase or a file?"
    mode = prompt()
    while mode.lower() != "phrase" and mode.lower() != "file":
        print mode
        print "Invalid mode. Please choose either 'phrase' or 'file'"
        mode = prompt()
    if mode.lower() == "phrase":
        count, num_words = phrase_mode(prompt)
    elif mode.lower() == "file":
        count, num_words = file_mode(prompt)
    return count, num_words


def main(prompt):
    print "Welcome."
    count, num_words = get_input(prompt)
    print "There were a total of %d words counted." % num_words
    if num_words < 10:
        print "The %d most used words were:" % num_words
    else:
        print "The 10 most used words were:"
    print count.most_common(10)

if __name__ == "__main__":
    main(MY_PROMPT)
