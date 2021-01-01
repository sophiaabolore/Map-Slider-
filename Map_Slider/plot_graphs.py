"""CSC110 Fall 2020 Final Project: Plot Graphs

Description
===============================
This python module contains functions that plot
the graphs based off of the emissions dataset

Copyright Information
===============================
This file is Copyright (c) 2020 Emily Chang, Michelle Chernyi, and Sophia Abolore.
"""
from typing import List, Tuple
import csv
import pandas as pd
import plotly.graph_objects as go


def separate_by_year_graph(year: int) -> None:
    """extract the data from the year given

    Preconditions:
        - 1964 <= year <= 2013
    """
    # read the file
    emissions = pd.read_csv('emissions-edited-graph.csv', engine='python')
    index = 0
    # finds the first index that the given year shows up in
    for i in range(0, len(emissions)):
        if emissions['Year'][i] == year:
            index = i
            break
    lst = []
    # adds the year, country and total for the data
    # that is at the given year
    while index < len(emissions) and emissions['Year'][index] == year:
        lst.append([emissions['Year'][index],
                    emissions['Country'][index],
                    emissions['Total'][index]])
        index += 1

    # overwrites the dataset with the new data for the given year
    emissions_by_year_graph = pd.DataFrame(lst, columns=['Year', 'Name', 'Total'])
    emissions_by_year_graph.to_csv('emissions-by-year-graph.csv')


def plot_graph() -> None:
    """plot bar graph based off of the current year in the emissions-by-year-graph.csv file"""
    # reads the file and sets the correct values into the variables
    data, countries, year = read_csv_data('emissions-by-year-graph.csv')
    fig = go.Figure(data=[go.Bar(name='CO2', x=countries, y=data), ])
    title = f'CO2 Emissions ' + year
    fig.update_layout(barmode='stack',
                      title=title,
                      xaxis_title='Countries',
                      yaxis_title='CO2 Emissions (million metric tons)')
    fig.show()


def read_csv_data(filepath: str) -> Tuple[List[str], List[str], str]:
    """Return a tuple containing a list of the CO2 totals, a list of the country names
    and the year.

    Preconditions:
        - filepath refers to a csv file in the format of
          emissions-by-year.csv
          (i.e., could be that file or a different file in the same format)
    """
    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip header row
        next(reader)

        # accumulators for the totals and country names
        data_so_far = []
        countries = []
        year = 0
        for row in reader:
            totals = row[3]
            names = row[2]
            year = row[1]

            data_so_far.append(totals)
            countries.append(names)

    return (data_so_far, countries, year)


if __name__ == '__main__':
    import python_ta.contracts
    import doctest

    python_ta.check_all(config={
        'extra-imports': ['pandas', 'python_ta.contracts', 'plotly.graph_objects', 'csv'],
        'allowed-io': ['read_csv_data'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
    python_ta.contracts.check_all_contracts()
    doctest.testmod()
