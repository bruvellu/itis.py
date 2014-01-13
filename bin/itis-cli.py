#! /usr/bin/env python

import sys
import os

from optparse import OptionParser

sys.path.append(os.path.abspath(".."))

from itis.itis import Itis

def scientific_lookup(name):
    itis = Itis()
    return itis.search_by_scientific_name(name)

# Unsupported
def common_lookup(name):
    itis = Itis()
    return itis.search_by_common_name(name)

def main():
    op = OptionParser()
    op.add_option("-s", "--scientific-name", dest="scientific_name",
                  help="Lookup an organism by its scientific name.")
    op.add_option("-c", "--common-name", dest="common_name",
                  help="Lookup an organism by its common name.")

    (options, args) = op.parse_args()
    if options.scientific_name:
        print scientific_lookup(options.scientific_name)
    if options.common_name:
        print common_lookup(options.common_name)

if __name__ == "__main__":
    main()
