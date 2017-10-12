#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Finds (and tries to fix) postal codes which don't match \d\d-\d\d\d regexp.
"""

import xml.etree.cElementTree as ET
import re
import pprint


OSMFILE = "melbourne_australia.osm"

VALID_POSTAL = re.compile('\d\d\d\d')




def find_postal_issues(osmfile):
    """Returns dictionaries of valid and invalid postal codes; original values as dictionary keys, fixed values as values."""
    osm_file = open(osmfile, "r")
    valid = {}
    invalid = {}

    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == 'node':
            for tag in elem.iter('tag'):
                k = tag.get('k')
                if k == "addr:postcode":
                    v = tag.get('v')
                #v, fixed = fixed_postal_code(v)
                    if VALID_POSTAL.match(v):
                        valid[v] = v
                    else:
                        invalid[v] = v
    return valid, invalid


def report_postal_issues():
    """Prints a report about valid and invalid postal codes to stdout."""
    valid_postal, invalid_postal = find_postal_issues(OSMFILE)
    print '# of valid postal codes: ', len(valid_postal)
    print '# of invalid postal codes: ', len(invalid_postal)
    print
    print 'Invalid postal codes:'
    pprint.pprint(invalid_postal)


if __name__ == '__main__':
    report_postal_issues()
