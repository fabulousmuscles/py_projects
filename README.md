py_projects
========

This repository contains my solutions to some of [Karan Goel's Projects] (https://github.com/karan/Projects), written in
python 2.7.x. This is a work in progress, and the projects will be completed in no particular order. 
Only the projects I've completed will be listed, and I will likely be doing all kinds of stuff (that may or may not
be in Karan's Projects.).


Numbers
---------

[**Find PI to the Nth Digit**] (https://github.com/wreckage/py_projects/blob/master/Numbers/pi.py) - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.

[**Tax Calculator**] (https://github.com/wreckage/py_projects/blob/master/Numbers/tax.py) - Asks the user to 
enter a cost and a US state. It then returns the tax plus the total cost with tax.


Networking
---------

[**Port Scanner**] (https://github.com/wreckage/py_projects/blob/master/Networking/scan.py)- Enter an IP address and a port range where the program will then attempt to find open ports on the given computer by connecting to each of them. On any successful connections mark the port as open.


Text
---------

[**Count Words in a String**](https://github.com/wreckage/py_projects/blob/master/Text/count.py) - Counts the number 
of individual words in a string or file and display the top 10 most used words. Example of counting words in a file:

    $ python count.py
    Welcome.
    Would you like me to count the words in a phrase or a file?
    > file
    Enter a filename and I'll count the words in that file.
    > constitution.txt
    There were a total of 4613 words counted.
    The 10 most used words were:
    [('the', 423), ('of', 289), ('and', 193), ('shall', 191), ('be', 125), ('to', 114), 
    ('in', 89), ('states', 80), ('or', 79), ('united', 54)]

[**Random Gift Suggestions**] (https://github.com/wreckage/py_projects/blob/master/Text/gifts.py) - Enter various 
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
