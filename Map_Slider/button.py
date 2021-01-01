"""CSC110 Fall 2020 Final Project: Button

Description
===============================
This Python module contains the Button
dataclass that is used in main.py.

Copyright Information
===============================
This file is Copyright (c) 2020 Emily Chang, Michelle Chernyi, and Sophia Abolore.
"""
from dataclasses import dataclass
from typing import Tuple
import pygame
from pygame import surface
import pygame.font


@dataclass
class Button:
    """button class for an interactive button that can be put onto a pygame surface

    Instance Attributes:
        - colour: colour of the button
        - x: x-coordinate of the button
        - y: y-coordinate of the button
        - width: the width of the button
        - height: the height of the button
        - text: the text that should appear on the button

    Representation Invariants:
        - 0 <= self.colour[0] <= 255
        - 0 <= self.colour[1] <= 255
        - 0 <= self.colour[2] <= 255
        - self.text != ''
    """
    colour: Tuple[int, int, int]
    x: int
    y: int
    width: int
    height: int
    text: str

    def draw(self, win: surface, outline: Tuple[int, int, int]) -> None:
        """draws the button on the surface that is passed in

        Preconditions:
            - 0 <= outline[0] <= 255
            - 0 <= outline[1] <= 255
            - 0 <= outline[2] <= 255
        """
        pygame.draw.rect(win, outline,
                         (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height), 0)

        font = pygame.font.SysFont('timesnewromanms', 60)
        text = font.render(self.text, True, (0, 0, 0))
        win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2),
            self.y + (self.height / 2 - text.get_height() / 2)))

    def hover(self, pos: Tuple) -> bool:
        """returns True if the mouse is hovering over the button
        (returns True if pos is a coordinate that is contained by the button)
        """
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


if __name__ == '__main__':
    import python_ta.contracts
    import doctest

    python_ta.check_all(config={
        'extra-imports': ['pygame.font', 'python_ta.contracts', 'pygame', 'dataclasses'],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
    python_ta.contracts.check_all_contracts()
    doctest.testmod()
