#!/usr/bin/env python
# -*- coding: utf-8 -*-

import piece


class Knight(piece.Piece):
    '''Representing a knight piece
    
        Attributes :
        team : str : The team of the piece (white or black)
        name : str : The english name of the piece
        annotation : char : The piece letter for writting moves
        
        Methods :
        __init__ : Create a knight piece from Piece object
        get_all_moves : Returns all the possible moves by the knight 
    '''  
    
    
    def __init__(self, team):
        '''Create a knight piece from Piece object
        
        Arguments : 
        team : str : wether the piece is white or black
        '''
        
        super().__init__(team)
        self.name = 'Knight'
        self.annotation = 'N'
        
       
    def get_all_moves(self, x, y, board):
        '''Returns all the possible moves by the knight
        
        Arguments : 
        x : integer : the x position of the rook on the board 
        y : integer : the y position of the rook on the board 
        board : Board : the current board to play the move 
        
        Returns : list : containing all moves as [x_destination, y_destination]
        '''
        
        # Returns the distance between two squares (x0, y0) (x1, y1)
        def dist(x0, y0, x1, y1):
            return (x0 - x1) ** 2 + (y0 - y1) ** 2
    
    
        res = []
        
        # Enumerate over all the reachable squares by the knight
        for x2 in set(range(8)).intersection(range(x - 2, x + 3)):
            for y2 in set(range(8)).intersection(range(y - 2, y + 3)):
                
                # Basically the squares where the knight can go to
                if dist(x, y, x2, y2) == 5:
                    piece_on_dest = board.get_case_from_coord(x2, y2).piece
                    if piece_on_dest is None or piece_on_dest.team != self.team:
                        res.append([x2, y2])
                        
        return sorted(res)
