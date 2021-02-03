#!/usr/bin/env python
# -*- coding: utf-8 -*-

import case


class Board:
    ''' This class represents the board of the chess game.
    This class is the only listener in our program.
    As we never touche other sub classes (pieces...), this on is the interface
    bewtween us and these sub classes.

    Attributes
    ----------
    board : list of Case object
        the main board 
    graveyard : dict
        the place where took pieces go

    Methods
    -------
    '''
    
    def __init__(self):
        '''
        Constructs and initialize all the necessary attributes for the board 
        object.
        
        Parameters
        ----------
        '''
        
        # the pieces_position.config object's got the initial position
        with open('datas/pieces_position.config', 'r') as f:
            pieces_positions = eval(''.join(f.readlines()))
            self.board = [case.Case(i, pieces_positions) for i in range(64)]
            self.graveyard = {
                'white': [],
                'black': []
            }
        
    # TODO a prettyprint