#!/usr/bin/env python
# -*- coding: utf-8 -*-

import piece
import rook, bishop

class Queen(piece.Piece):
    '''Representing a queen piece
    
        Attributes :
        team : str : The team of the piece (white or black)
        name : str : The english name of the piece
        annotation : char : The piece letter for writting moves
        
        Methods :
        __init__ : Create a queen piece from Piece object
        get_all_moves : Returns all the possible moves by the queen 
    '''  
    
    
    def __init__(self, team):
        '''Create a queen piece from Piece object
        
        Arguments : 
        team : str : whether the piece is white or black
        '''
        super().__init__(team)
        self.name = 'Queen'
        self.annotation = 'Q'

        
    def get_all_moves(self, x, y, board):
        '''Returns all the possible moves by the queen
        In fact the queen move is the combination of a bishop and a rook 
                
        Arguments : 
        x : integer : the x position of the rook on the board 
        y : integer : the y position of the rook on the board 
        board : Board : the current board to play the move 
        
        Returns : list : containing all moves as [x_destination, y_destination]
        '''
        
        return sorted(bishop.Bishop(self.team).get_all_moves(x, y, board) + \
            rook.Rook(self.team).get_all_moves(x, y, board))