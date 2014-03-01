py_projects
========

This repository contains my solutions to some of [Karan Goel's Projects] (https://github.com/karan/Projects), written in
python 2.7.x. This is a work in progress, and the projects will be completed in no particular order. 
Only the projects I've completed will be listed, and I will likely be doing all kinds of stuff (that may or may not
be in Karan's Projects.).


Numbers
---------

[**Find PI to the Nth Digit**] (https://github.com/fabulousmuscles/py_projects/blob/master/Numbers/pi.py) - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.


Networking
---------

[**Port Scanner**] (https://github.com/fabulousmuscles/py_projects/blob/master/Networking/scan.py)- Enter an IP address and a port range where the program will then attempt to find open ports on the given computer by connecting to each of them. On any successful connections mark the port as open.


Text
---------
[**Random Gift Suggestions**] (https://github.com/fabulousmuscles/py_projects/blob/master/Text/gifts.py) - Enter various 
gifts for certain people when you think of them. When its time to give them a gift (xmas, birthday, anniversary) it will 
randomly pick one. Creates a folder called 'gifts' in the current working directory using os.getcwd(), then stores gift
ideas in a JSON file for each person. Example usage:

    $ python gifts.py add
    Enter the name of the person who's gift idea you'd like to record.
    If you haven't recorded gifts for this person yet, a record will be created.
    > Ed
    Enter the gift you'd like to record for Ed
    > firewall
    The gift 'firewall' for Ed was successfully recorded.

You can get a random gift like this:

    $ python gifts.py get
    Enter the name of the person and I'll give you a random gift from the gifts you've set.
    > Ed
    The gift I've chosen is... USB Stick.
