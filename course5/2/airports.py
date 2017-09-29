#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Complete the 'extract_airports()' function so that it returns a list of airport
codes, excluding any combinations like "All".

Refer to the 'options.html' file in the tab above for a stripped down version
of what is actually on the website. The test() assertions are based on the
given file.
"""

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        options=soup.find_all("option")
        for item in options:
            if len(item["value"])==3:
                if item["value"]!="All":
                    data.append(item["value"])
    return data


def test():
    data = extract_airports(html_page)
    print data
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

if __name__ == "__main__":
    test()
