"""CSC110 Fall 2020 Final Project: Map

Description
===============================
This Python module contains functions whose purpose is to produce a
map for a specific year.

They are helper functions that are called upon in the main module, main.py .

if you want to see just one map that is not interactive,
they will create a dataset/ map when run
however, you do not need to run them. They will be run in main.py .

Copyright Information
===============================
This file is Copyright (c) 2020 Emily Chang, Michelle Chernyi, and Sophia Abolore.
"""
import pandas as pd
import geopandas
import matplotlib.pyplot as plt


def separate_by_year_map(year: int) -> None:
    """extracts the data from data set for the year given
    Preconditions:
         - 1964 <= year <= 2013
    """
    emissions = pd.read_csv('emissions-map.csv', engine='python')
    index = 0
    for i in range(0, len(emissions)):
        if emissions['Year'][i] == year:
            index = i
            break
    lst = []
    while index < len(emissions) and emissions['Year'][index] == year:
        lst.append([emissions['Year'][index],
                    emissions['Country'][index], emissions['Total'][index]])
        index += 1

    emissions_by_year = pd.DataFrame(lst, columns=['Year', 'Name', 'Total'])
    emissions_by_year.to_csv('emissions-by-year-map.csv')


def create_map(year: int) -> None:
    """ creates a map using co2 emissions dataset by year and
    dataset of country geometry available in geopandas.
    function merges datasets then produces map with legend and title
    Preconditions:
        - 1964 <= year <= 2013
    """
    separate_by_year_map(year)
    emissions_file = pd.read_csv('emissions-by-year-map.csv', engine='python')
    # countries and geomtry data file
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    # removes antartica from map
    world = world[(world.pop_est > 0) & (world.name != "Antarctica")]
    # connect name of country to geometry
    country_shapes = world[['geometry', 'iso_a3']]
    country_names = world[['name', 'iso_a3']]
    country_shapes = country_shapes.merge(country_names, on='iso_a3')
    # ensure both files have a matching column
    country_shapes['Name'] = country_shapes['name'].apply(lambda x: x.upper())
    # merge data
    map_data = pd.merge(country_shapes, emissions_file, how='left', on='Name')

    _, ax = plt.subplots(1, 1, figsize=(14, 4))
    # plot map and legend
    map_data.plot(column='Total', ax=ax, legend=True, cmap='YlOrRd', scheme='quantiles', k=10,
                  legend_kwds={'bbox_to_anchor': (1.35, 0.9)},
                  missing_kwds={"color": "lightgrey", "edgecolor":
                                "red", "hatch": "///", "label": "Missing values"})
    # title of map
    ax.set_title("C02 Emission Levels by Country (In million metric tons) In " + str(year))


if __name__ == '__main__':
    import python_ta.contracts
    import doctest

    python_ta.check_all(config={
        'extra-imports': ['pandas', 'geopandas', 'matplotlib.pyplot',
                          'python_ta.contracts', 'doctest'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
    python_ta.contracts.check_all_contracts()
    doctest.testmod()
