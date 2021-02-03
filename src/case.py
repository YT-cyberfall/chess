#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Case:
    ''' This class represents a square of the board.

    Attributes
    ----------
    x : int 
        the (A,B,C,D,E,F,G,H) piece position as integer 
    y : int 
        the ordonate piece position as integer 
    piece : Piece object
        the piece which is on the square
    color : str
        the square color < black or white >

    Methods
    -------
    '''
    def __init__(self, num, pieces_positions):
        '''
        Constructs and initialize all the necessary attributes for the square 
        object.
        
        Parameters
        num : 0 <= int <= 63 (number of square)
            the index of the case to initialize
        pieces_position : dict 
            the initial chess board position 
        ----------
        '''
        
        # Attribute assignement
        self.x = num % 8
        self.y = num // 8
        assert 0 <= max(self.x, self.y) < 8
        self.color = ('white', 'black')[self.x % 2 == self.y % 2]
        self.piece = pieces_positions.get((self.x, self.y))
