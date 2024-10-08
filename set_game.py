# Set Game
# Peyton Wall & Prof. O
# 2024-10-07 Created the SetCard and make_deck functions and made their doctest
# 2024-10-08 Did all the other functions and finished up writing all the doctests

from enum import Enum
from random import shuffle

class Fill(Enum):
    EMPTY = 0
    SHADED = 1
    FILLED = 2
    
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Shape(Enum):
    QUAD = 5
    OVAL = 17
    PYRAMID = 234

class SetCard:
    def __init__(self, number, fill, color, shape):
        '''int in [1,3], Fill, Color, Shape -> SetCard
        >>> card = SetCard(1, Fill.FILLED, Color.RED, Shape.QUAD)
        >>> card.number
        1
        >>> card.fill
        <Fill.FILLED: 2>
        >>> card.color
        <Color.RED: 1>
        >>> card.shape
        <Shape.QUAD: 5>

        >>> card = SetCard(2, Fill.EMPTY, Color.GREEN, Shape.OVAL)
        >>> card.number
        2
        >>> card.fill
        <Fill.EMPTY: 0>
        >>> card.color
        <Color.GREEN: 2>
        >>> card.shape
        <Shape.OVAL: 17>

        >>> card = SetCard(3, Fill.SHADED, Color.BLUE, Shape.PYRAMID)
        >>> card.number
        3
        >>> card.fill
        <Fill.SHADED: 1>
        >>> card.color
        <Color.BLUE: 3>
        >>> card.shape
        <Shape.PYRAMID: 234>
        '''
        pass
        self.number = number
        self.fill = fill
        self.color = color
        self.shape = shape

    def __str__(self):
        '''Human-readable representation of this card.
        >>> str(SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL))
        '1SBO'
        >>> str(SetCard(2, Fill.EMPTY, Color.RED, Shape.QUAD))
        '2ERQ'
        >>> str(SetCard(3, Fill.FILLED, Color.GREEN, Shape.PYRAMID))
        '3FGP'
        '''
        pass
        return f"{self.number}{self.fill.name[0]}{self.color.name[0]}{self.shape.name[0]}"
    
    def __repr__(self):
        '''Python code to recreate this card.
        >>> SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL)
        SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL)
        >>> repr(SetCard(2,Fill.EMPTY,Color.RED,Shape.QUAD))
        'SetCard(2, Fill.EMPTY, Color.RED, Shape.QUAD)'
        '''
        pass
        return f"SetCard({self.number}, {self.fill}, {self.color}, {self.shape})"
    
    def third_card(self, other):
        '''Returns the third card that makes a set with self and other.
        >>> card1 = SetCard(1, Fill.EMPTY, Color.RED, Shape.QUAD)
        >>> card2 = SetCard(2, Fill.SHADED, Color.BLUE, Shape.OVAL)
        >>> card3 = SetCard(3, Fill.FILLED, Color.GREEN, Shape.PYRAMID)
        >>> print(card1.third_card(card2))
        3FGP
        >>> print(card2.third_card(card3))
        1ERQ
        >>> print(card1.third_card(card3))
        2SBO
        '''
        pass
        # Number: ensure it's valid and that the sum of the three card numbers is divisible by 3
        number = (3 - ((self.number + other.number) % 3)) % 3
        if number == 0:
            number = 3
        
        # Fill: either all same or all different
        if self.fill == other.fill:
            fill = self.fill
        else:
            fill = (set(Fill) - {self.fill, other.fill}).pop()

        # Color: either all same or all different
        if self.color == other.color:
            color = self.color
        else:
            color = (set(Color) - {self.color, other.color}).pop()

        # Shape: either all same or all different
        if self.shape == other.shape:
            shape = self.shape
        else:
            shape = (set(Shape) - {self.shape, other.shape}).pop()

        return SetCard(number, fill, color, shape)

def make_deck():
    '''Returns a list containing a complete Set deck with 81 unique cards.
    >>> deck = make_deck()
    >>> len(deck)
    81
    >>> isinstance(deck, list)
    True
    '''
    deck = [SetCard(number, fill, color, shape)
            for number in range(1, 4)
            for fill in Fill
            for color in Color
            for shape in Shape]
    shuffle(deck)
    return deck

def is_set(card1, card2, card3):
    '''Determines whether the 3 cards make a set.
    >>> card1 = SetCard(1, Fill.FILLED, Color.RED, Shape.QUAD)
    >>> card2 = SetCard(2, Fill.SHADED, Color.GREEN, Shape.OVAL)
    >>> card3 = SetCard(3, Fill.EMPTY, Color.BLUE, Shape.PYRAMID)
    >>> is_set(card1, card2, card3)
    True

    >>> card4 = SetCard(1, Fill.FILLED, Color.RED, Shape.QUAD)
    >>> card5 = SetCard(2, Fill.SHADED, Color.RED, Shape.QUAD)
    >>> card6 = SetCard(3, Fill.EMPTY, Color.RED, Shape.QUAD)
    >>> is_set(card4, card5, card6)
    True

    >>> card7 = SetCard(1, Fill.FILLED, Color.RED, Shape.QUAD)
    >>> card8 = SetCard(2, Fill.SHADED, Color.RED, Shape.QUAD)
    >>> card9 = SetCard(3, Fill.EMPTY, Color.RED, Shape.OVAL)  # Different shape
    >>> is_set(card7, card8, card9)
    False
    '''
    for attribute in ['number', 'fill', 'color', 'shape']:
        values = {getattr(card1, attribute), getattr(card2, attribute), getattr(card3, attribute)}
        if len(values) not in [1, 3]:
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
