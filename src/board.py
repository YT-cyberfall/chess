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
    
    
    def pprint(self): 
        '''This method print the board in the console''' 
        
        # TODO remplacer par Piece
        print('   ' + '_' * 8 * 3)
        for i in range(0, 64, 8):
            print((i // 8) + 1, end='  ')
            print('|', end='')
            print(*[x.piece for x in self.board[i:i+8]], sep='|', end='')
            print('|')
            print('   ' + '_' * 8 * 3)
        print( '   ', end=' ')
        print(*[chr(x) for x in range(65, 73)], sep='  ')

        
        