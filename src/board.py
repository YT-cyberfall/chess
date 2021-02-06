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
            pieces_positions = eval(f.read())
        self.board = [case.Case(i, pieces_positions) for i in range(64)]
        self.graveyard = {
            'white': [],
            'black': []
        }
    
    
    def pprint(self): 
        '''This method print the board in the console''' 
        
        # Reverse the board to easily printting it with the white view
        rev_board = [self.board[::-1][i:i+8][::-1] for i in range (0, 64, 8)]
   
        # Print algorithm
        print('    ' + '_' * 8 * 4)
        for k, v in enumerate(rev_board):
            print(8 - k , end='  ')
            print('|', end=' ')
            print(
                *[x.piece.annotation if x.piece else ' ' for x in v], 
                sep=' | ',
                end='')
            print(' |')
            print('    ' + '_' * 8 * 4)
        print( '    ', end=' ')
        print(*[chr(x) for x in range(65, 73)], sep='   ')
        
    # TODO
    def play_a_move(self, origin, destination):
        '''Move the piece at origin to destination. The move is made only if the
        square is empty or took by opponent.
        Basically, origin always become : case.piece = None, and destination 
        always become : case.piece = origin piece.
        This function also feed the graveyard if necessary
        '''
        import pprint
        case_origin = self.board[origin[0] + origin[1] * 8]
        case_destination = self.board[destination[0] + destination[1] * 8]
        print(case_origin)
        print(case_destination)

        
        