#!/usr/bin/env python
# -*- coding: utf-8 -*-

import case

class Board:
    ''' This class represents the board of the chess game.
    This class is the only listener in our program.
    As we never touche other sub classes (pieces...), this on is the interface
    bewtween us and these sub classes.

    Attributes :
    board : list of Case : the main board 
    graveyard : dict : the place where took pieces go
    
    Methods :
    __init__ : Constructs and initialize all the necessary attributes for the 
    board object.
    pprint : Prints the board in the console
    get_move_for_square : 
    get_case_from_coord :
    play_a_move : 
    move_to_note : 
    '''
    
    def __init__(self):
        '''
        Constructs and initialize all the necessary attributes for the board 
        object.
        '''
        
        try :
            
            # The pieces_position.config object's got the initial position
            with open('datas/pieces_position.config', 'r') as f:
                pieces_positions = eval(f.read())
                
            # Creating the Cases structs for each square
            self.board = [case.Case(i, pieces_positions) for i in range(64)]
            
            # At the begining of the game, the graveyard is empty
            self.graveyard = {
                'white': [],
                'black': []
            }
            
            # The history of the game
            self.history = []
            
            # The number of the current move
            self.move_num = 1

        except EnvironmentError:
            print('Unable to open the config position file')
    
    
    def pprint(self): 
        '''Prints the board in the console''' 
        
        # Reverse the board to easily printing it with the white view
        rev_board = [self.board[::-1][i:i + 8][::-1] for i in range (0, 64, 8)]
   
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
        '''Get the possible move list for the piece located at (x, y)
        
        Attributes :
        x : int : The x coordinate of the square
        y : int : The y coordinate of the square
        '''
        
        piece = self.get_case_from_coord(x, y).piece
        return piece.get_all_moves(x, y, self) if piece else []
        
        
    def get_case_from_coord(self, x, y):
        '''Get the square located on the (x, y) position
        
        Attributes :
        x : int : The x coordinate of the square
        y : int : The y coordinate of the square
        '''
        
        try:
            
            # The coordinates have to be outo the board
             if any(v not in range(8) for v in (x, y)):
                 raise ValueError('Illegal coordinates -> out of the board')
             
             return self.board[y * 8 + x]
         
        except AssertionError as e:
            print(e)
            
        
    def play_a_move(self, origin, destination):
        '''Move the piece at origin to destination. The move is made only if the
        square is empty or took by opponent.
        Basically, origin always become : case.piece = None, and destination 
        always become : case.piece = origin piece.
        This function also feed the graveyard if necessary.
        
        Attributes :
        origin : tuple of int : The coordinate of the origin square as (x, y)
        destination : tuple of int : The coordinate of the dest square as (x, y)
        '''
        
        try:
           
           # The first part is about testing args coherence
           
           # A move can not be from (x, y) to (x, y)
            if origin == destination:
                raise ValueError('Move options are illegal -> '
                                     'identical position')
            
            # All moves coordinates should be in range(8)
            if not all([coord in range(8) for coord in origin + destination]):
                raise ValueError('Move options are illegal -> '
                                     'Out of the board')
                
            # Updating the move number if it already has been writen 2 times
            # This is needed for the history
            if len([move for move in self.history if \
                move.startswith(str(self.move_num))]) == 2:
                   self.move_num += 1
            
            # The move is write out inside the history
            self.history.append(self.move_to_note(origin, destination))
            
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
                self.send_to_grave(case_destination)
                
            # Final assignements of the move
            case_destination.piece = case_origin.piece
            case_origin.piece = None   
            
            # A pawn only can move forward by two square when it's his first
            # move
            if case_destination.piece.name == 'Pawn':
                case_destination.piece.first_move = False
            
        except AssertionError as e:
            print(e)
            
    
    #TODO 
    def move_to_note(self, origin, destination):
        '''This function takes a move and write it as chess formatted
        NxB5 etc
        
        Arguments :
        origin : tuple of int : The coordinate of the origin square as (x, y)
        destination : tuple of int : The coordinate of the dest square as (x, y)
        '''
        return f'{self.move_num}. {origin}{destination}'
    
    
    def send_to_grave(self, case):
        '''This function put the piece on case in the gravyard
        
        Arguments :
        case : Case : the case on which there's the piece to kill
        '''
        self.graveyard[case.piece.team].append(case.piece)
        
    def _get_last_move(self, display_move_num=False):
        '''Returns the last move played
        
        Arguments :
        display_move_num : bool : if we display the move number or not
        '''
        last_move = None if len(self.history) == 0 else self.history[-1]
        return last_move if display_move_num or last_move is None else \
            last_move.split('.')[1] 
            
        
         
                

        
        