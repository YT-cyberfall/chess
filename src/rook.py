#!/usr/bin/env python
# -*- coding: utf-8 -*-

import piece


class Rook(piece.Piece):
    '''Representing a rook piece
    
        Attributes :
        team : str : The team of the piece (white or black)
        name : str : The english name of the piece
        annotation : char : The piece letter for writting moves
        first_move : bool : Whether the piece has move or not
        
        Methods :
        __init__ : Create a rook piece from Piece object
        get_all_moves : Returns all the possible moves by the Rook 
    '''
    
    
    def __init__(self, team):
        '''Create a rook piece from Piece object
        
        Arguments : 
        team : str : wether the piece is white or black
        '''
        
        super().__init__(team)
        self.name = 'Rook'
        self.annotation = 'R'
        self.first_move = True
            
    
    def get_all_moves(self, x, y, board):
        '''Returns all the possible moves by the Rook
        
        Arguments : 
        x : integer : the x position of the rook on the board 
        y : integer : the y position of the rook on the board 
        board : Board : the current board to play the move 
        
        Returns : list : containing all moves as [x_destination, y_destination]
        '''
        
        res = []
        
        # The vertical possibilities
        for x_direction in [range(x)[::-1], range(x + 1, 8)]:
            for x2 in x_direction:
                
                # The piece onto the case to go to (None if any)
                piece_on_dest = board.get_case_from_coord(x2, y).piece
                if piece_on_dest is None:
                    res.append([x2, y])
                elif piece_on_dest.team != self.team:
                    res.append([x2, y])
                    break
                else:
                    break
                
        # The horizontal possibilities
        for y_direction in [range(y)[::-1], range(y + 1, 8)]:
            for y2 in y_direction:
                
                # The piece onto the case to go to (None if any)
                piece_on_dest = board.get_case_from_coord(x, y2).piece
                if piece_on_dest is None:
                    res.append([x, y2])
                elif piece_on_dest.team != self.team:
                    res.append([x, y2])
                    break
                else:
                    break

        return sorted(res)
        