#!/usr/bin/env python

## Random Gift Suggestions ##
# Enter various gifts for certain people when you think of them. When its time
# to give them a gift (xmas, birthday, anniversary) it will randomly pick one.

import json
import os
from random import randint
from sys import argv, stderr


MY_PROMPT = lambda: raw_input("> ")
folder = os.path.join(os.getcwd(), "gifts")
path = lambda person: os.path.join(
    folder, "%s.json" % person.replace(" ", "-").lower()
)


def new_person(filename, person, gift):
    """
    Create a new json file with the given filename, and in it record
    the person and the gift idea.
    """
    with open(filename, "w") as f:
        json.dump({"name": person, "gifts": [gift]}, f, indent=4)


def add_gift(filename, person, gift):
    """Add a gift to a person's json file, or create one if it doesn't exist"""
    try:
        with open(filename, "r") as f:
            obj = json.load(f)
            obj['gifts'].append(gift)
        with open(filename, "w") as f:
            json.dump(obj, f, indent=4)
    # The file may not exist, or it may be empty. Either way create a new one.
    except Exception:
        new_person(filename, person, gift)
    print "The gift '%s' for %s was successfully recorded." % (gift, person)


def create(prompt):
    """
    Collect the name and gift idea from the person. Then add the gift idea
    to the .json file for that person. If the file doesn't exist, add_gift()
    will call new_person() and create one.
    """
    print("Enter the name of the person who's gift idea you'd like to record."
          "\nIf you haven't recorded gifts for this person yet, "
          "a record will be created.")
    person = prompt()
    print "Enter the gift you'd like to record for %s." % person
    gift = prompt()
    filename = path(person)
    add_gift(filename, person, gift)


def get_gifts(prompt):
    """Get a random gift from the json file for the given person."""
    print("Enter the name of the person and I'll give you a random gift from "
          "the gifts you've set.")
    person = prompt()
    try:
        with open(path(person), "r") as f:
            obj = json.load(f)
    except Exception:
        print "A record of that person's gifts doesn't exist."
        exit(1)

    gifts = obj['gifts']
    rand = randint(0, len(gifts) - 1)
    print "The gift I've chosen is... %s." % gifts[rand]


if __name__ == "__main__":
    if argv[1:] == ["add"]:
        try:
            os.makedirs(folder)
        except Exception as e:
            if e.errno == 17:
                pass
            else:
                print e
                exit(1)
        create(MY_PROMPT)
    elif argv[1:] == ["get"]:
        get_gifts(MY_PROMPT)
    else:
        print >>stderr, 'usage: gifts.py add|get'
