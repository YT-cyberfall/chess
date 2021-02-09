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
        
        # The pieces_position.config object's got the initial position
        with open('datas/pieces_position.config', 'r') as f:
            pieces_positions = eval(f.read())
            
        # creating the Cases structs for each square
        self.board = [case.Case(i, pieces_positions) for i in range(64)]
        
        # At the begining of the game, the graveyard is empty
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
        
        
    def get_move_for_square(self, x, y):
        '''Get the possible move list for a sqaure(x, y)'''
        case = self.get_case_from_coord(x,y)
        return case.piece.get_all_moves(x,y, self)
        
        
        
    def get_case_from_coord(self, x, y):
        
        try:
             if (x not in range(8)) or (y not in range(8)):
                 raise ValueError('Coordinates are illegal -> out of the board')
             return self.board[y * 8 + x]
        except AssertionError as e:
            print(e)
            
        
    def play_a_move(self, origin, destination):
        '''Move the piece at origin to destination. The move is made only if the
        square is empty or took by opponent.
        Basically, origin always become : case.piece = None, and destination 
        always become : case.piece = origin piece.
        This function also feed the graveyard if necessary.
        '''
        
        try:
           
           # The first part is about testing args coherence
           
           # A move can not be from (x, y) to (x, y)
            if origin == destination:
                raise ValueError('Move options are illegal -> '
                                     'identical position')
            
            # All moves coordinates should be in range(8)
            if False in [0 <= coord < 8 for coord in origin + destination]:
                raise ValueError('Move options are illegal -> '
                                     'Out of the board')
                
            # Getting associated Case struct for args, for easier operations
            case_origin = self.board[origin[0] + origin[1] * 8]
            case_destination = self.board[destination[0] + destination[1] * 8]
            
            # The move is made by a Piece, so the origin case can not be empty
            if case_origin.piece is None:
                raise ValueError('Move options are illegal -> '
                                 'origin doesnt have piece on it')
                
            # A piece can not move onto a square took by an allies
            if case_destination.piece is not None and \
                case_origin.piece.team == case_destination.piece.team:
                raise ValueError('Move options are illegal -> '
                                 'destination took y allies')
            
            # If there's a piece on the destination square, this piece is dead
            if case_destination.piece:
                self.graveyard[case_destination.piece.team].\
                    append(case_destination.piece)
                    
            # Final assignements of the move
            case_destination.piece = case_origin.piece
            case_origin.piece = None   
            
        except AssertionError as e:
            print(e)
            
        
         
                

        
        