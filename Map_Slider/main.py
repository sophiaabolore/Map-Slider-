"""CSC110 Fall 2020 Final Project: Main

Description
===============================
This python module generates the year, based off the mouse
position, loads an image for that year and displays it along
with the button and slider on a pygame surface.

Copyright Information
===============================
This file is Copyright (c) 2020 Emily Chang, Michelle Chernyi, and Sophia Abolore.
"""
from PIL import Image
import pygame
import pygame.locals
import matplotlib.pyplot as plt
from map import create_map
from plot_graphs import plot_graph, separate_by_year_graph
from button import Button
from totals import totals


def load_picture(year: int) -> str:
    """ Generates a string representing the filename of the map of the inputed year
    #NOTE: This function should return the same string regardless of it's inputed year
    Preconditions:
        - 1964 <= year <= 2013

    >>> load_picture(1965)
    'world.jpg'
    >>> load_picture(1987)
    'world.jpg'
    """
    separate_by_year_graph(year)
    create_map(year)
    plt.savefig('world.jpg')
    plt.close(fig=None)
    image = Image.open('world.jpg')
    new_image = image.resize((1680, 480))
    new_image.save('world.jpg')
    return 'world.jpg'


def generate_year_from_pos(x: int) -> int:
    """Generates the year for the corresponding slider position on the surface
    Preconditions:
        - 0 <= x <= 1400
    >>> generate_year_from_pos(15)
    1964
    >>> generate_year_from_pos(1398)
    2013
    """
    year = x // 28 + 1964
    return year


def refresh_all(x: int, button: Button) -> None:
    """ resets screen with new map, creates blank screen,
    creates the slider, draws the button, loads the map, adds text

    Preconditions:
        - 0 <= x <= 1400
    """
    white = (255, 255, 255)
    black = pygame.Color(0, 0, 0)
    grey = pygame.Color(128, 128, 128)
    x1 = 1400
    y1 = 1400
    # create a surface object, image is drawn on it.
    width = 1400
    height = 1400

    display_surface = pygame.display.set_mode((1400, 1400))

    display_surface.fill(white)
    window_surface_obj = pygame.display.set_mode((width, height), 1, 16)

    pygame.draw.rect(window_surface_obj, white, pygame.locals.Rect(0, 0, x1, y1))
    pygame.draw.rect(window_surface_obj, black, pygame.locals.Rect(0, 20, width, 10))

    image = pygame.image.load(load_picture(generate_year_from_pos(x)))
    display_surface.blit(image, (-300, 200))

    pygame.draw.rect(window_surface_obj, grey, pygame.locals.Rect(x, 5, 10, 40))
    button.draw(display_surface, (0, 0, 0))

    font = pygame.font.SysFont('timesnewromanms', 40)
    # creates surface for text and chooses colours
    text = font.render(totals(), True, black, white)
    # creates rectangular object
    text_rect = text.get_rect()
    # location of text
    text_rect.center = (300, 100)
    # displays text on surface
    display_surface.blit(text, text_rect)

    pygame.display.update()


def display() -> None:
    """
    Creates the pygame surface and displays the map, button and slider on
    it by calling refresh_all(). This function intializes the pygame surface,
    creates the button and continually displays map, button and slider while
    the function is being run. It also controls the buttons functions depending
    on the position.
    """
    pygame.init()
    button = Button((255, 255, 255), 100, 755, 150, 50, 'Graph')

    # set the pygame window name
    pygame.display.set_caption('Image')

    # starting position
    x = 0

    refresh_all(x, button)

    while True:

        for event in pygame.event.get():

            # if event object type is QUIT then quit both the pygame and program
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()

                # quit the program.
                quit()

            if event.type == pygame.MOUSEBUTTONUP:

                pos = pygame.mouse.get_pos()

                is_refresh_all = True

                if button.hover(pos):
                    plot_graph()
                    is_refresh_all = False

                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                if y > 45:
                    is_refresh_all = False

                if is_refresh_all:
                    refresh_all(x, button)
