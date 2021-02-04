#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rook, knight, bishop, queen, king, pawn

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
        self.color = 'black' if self.x % 2 == self.y % 2 else 'white'
        piece_name = pieces_positions.get((self.x, self.y))
        self.piece = eval(f'{piece_name[0].lower()}.{piece_name[0]}("{piece_name[1]}")') if piece_name else None
