#!/usr/bin/env python
# -*- coding: utf-8 -*-

import piece


class King(piece.Piece):
    
    def __init__(self, team):
        '''Create a king piece from Piece object
        
        Arguments : 
        team : str : wether the piece is white or black
        
        Attributes :
        name : str : The english name of the piece
        annotation : char : The piece letter for writting moves
        first_move : bool : Whether the piece has move or not
        '''
        
        super().__init__(team)
        self.name = 'King'
        self.annotation = 'K'
        self.first_move = True
        
    
    def get_all_moves(self, x, y, board):
        '''Returns all the possible moves by the King
        
        Arguments : 
        x : integer : the x poissiotn of the king on the board 
        y : integer : the y poissiotn of the king on the board 
        board : Board : the current board to play the move 
        
        Returns : list : containing all moves as [x_destination, y_destination]
        '''
        
        # TODO Castle and not moving on a check square
        res = []
        
        for x2 in set(range(8)).intersection(range(x - 1, x + 2)):
            for y2 in set(range(8)).intersection(range(y - 1, y + 2)):
                
                piece_on_dest = board.get_case_from_coord(x2, y2).piece
                if piece_on_dest is None or piece_on_dest.team != self.team:
                    res.append([x2, y2])
            
        return sorted(res)       