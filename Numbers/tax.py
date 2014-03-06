#!/usr/bin/env python

###############################################################################
## Tax Calculator - Asks the user to enter a cost and a US state.
## It then returns the tax plus the total cost with tax.
###############################################################################
## NOTE: This program fetches the tax data from a website, so if
## you plan on using this regularly, it'd be a good idea to save the
## the fetched web data locally, then read from that instead of constantly
## connecting to the web site.
###############################################################################

import urllib2
import re

MY_PROMPT = lambda: raw_input("> ")
DOLLAR_PROMPT = lambda: raw_input("> $")


def main(prompt, dollar_prompt):
    print("Enter your state (full name only, "
          "abbreviations not currently supported).")
    state = prompt()
    print "Enter the cost of your item."
    cost = dollar_prompt()
    while True:
        try:
            cost = float(cost)
            break
        except Exception:
            print "Invalid input. Enter the cost of your item."
            cost = dollar_prompt()
    content = urllib2.urlopen(
        'http://www.salestaxinstitute.com/resources/rates'
    ).read()
    # save the file locally and read from it if using regularly:
    #open('taxes.txt', 'w').write(content)
    #content = open('taxes.txt', 'r').read()
    regex = '<td>%s</td>\n<td>(\d.\d+)' % state.title()
    tax = re.findall(regex, content)
    if not tax:
        print("Couldn't locate your state. Please try again with a "
              "valid US state.")
        exit(1)
    tax = float(tax[0])
    total_tax = (tax / 100) * cost
    total = cost + total_tax
    print "The tax rate is: %{:.3f}".format(tax)
    print "Total tax that must be paid: ${:.2f}".format(total_tax)
    print "Total cost with tax: ${:.2f}".format(total)

if __name__ == "__main__":
    main(MY_PROMPT, DOLLAR_PROMPT)
