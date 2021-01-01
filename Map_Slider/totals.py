"""CSC110 Fall 2020 Final Project: Totals

Description
===============================
This python module calculates the total emissions for the year
that is currently in the emissions-by-year-graph.csv file.

Copyright Information
===============================
This file is Copyright (c) 2020 Emily Chang, Michelle Chernyi, and Sophia Abolore.
"""
import pandas as pd


def totals() -> str:
    """return the total of all the emissions from that year in a string
    """
    emissions = pd.read_csv('emissions-by-year-graph.csv', engine='python')
    total = sum(emissions['Total'])
    return 'Total: ' + str(total) + ' million metric tons'


if __name__ == '__main__':
    import python_ta.contracts
    import doctest

    python_ta.check_all(config={
        'extra-imports': ['pandas', 'python_ta.contracts'],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
    python_ta.contracts.check_all_contracts()
    doctest.testmod()
