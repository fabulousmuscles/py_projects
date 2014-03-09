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

STATES = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}


def get_tax(state):
    print "Getting tax rate..."
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
    print "Done!"
    return tax


def get_input(prompt, dollar_prompt):
    print "Enter your state (full name or abbreviation)"
    state = prompt()
    while True:
        if len(state) == 2:
            if state.upper() in STATES.keys():
                    state = STATES[state.upper()]
                    break
            else:
                print "Invalid abbreviation. Please try again."
                state = prompt()
        else:
            if state.title() not in STATES.values():
                print "Invalid state name. Please try again."
                state = prompt()
            else:
                break
    print "Enter the cost of your item."
    cost = dollar_prompt()
    while True:
        try:
            cost = float(cost)
            break
        except Exception:
            print "Invalid input. Enter the cost of your item."
            cost = dollar_prompt()
    return state, cost


def main(prompt, dollar_prompt):
    state, cost = get_input(prompt, dollar_prompt)
    tax = get_tax(state)
    print "Computing tax..."
    total_tax = (tax / 100) * cost
    total = cost + total_tax
    print "Done!"
    print "The tax rate is: %{:.3f}".format(tax)
    print "Total tax that must be paid: ${:.2f}".format(total_tax)
    print "Total cost with tax: ${:.2f}".format(total)

if __name__ == "__main__":
    main(MY_PROMPT, DOLLAR_PROMPT)
