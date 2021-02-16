#!/usr/bin/env python
# -*- coding: utf-8 -*-

import piece


class Bishop(piece.Piece):
    '''Representing a bishop piece
    
        Attributes :
        team : str : The team of the piece (white or black)
        name : str : The english name of the piece
        annotation : char : The piece letter for writting moves
        
        Methods :
        __init__ : Create a bishop piece from Piece object
        get_all_moves : Returns all the possible moves by the Rook 
    '''    
    
    
    def __init__(self, team):
        '''Create a bishop piece from Piece object
        
        Arguments : 
        team : str : wether the piece is white or black
        '''
        
        super().__init__(team)
        self.name = 'Bishop'
        self.annotation = 'B'
        
        
    def get_all_moves(self, x, y, board):
        '''Returns all the possible moves by the Rook
        
        Arguments : 
        x : integer : the x position of the bishop on the board 
        y : integer : the y position of the bishop on the board 
        board : Board : the current board to play the move 
        
        Returns : list : containing all moves as [x_destination, y_destination]
        '''
        
        res = []
       
        # One loop for a direction to go
        for i in range(4):
            
            # For every square of the diagonal to check
            for space in range(1, x):
                
                # The cooridnates to check
                chk_x, chk_y = [
                    (x - space, y - space),
                    (x - space, y + space),
                    (x + space, y - space),
                    (x + space, y + space)][i]
                
                # the coordinates to check has to be inside the board
                if any([val not in range(8) for val in [chk_x, chk_y]]):
                    break
                
                # The piece onto the case to go to (None if any)
                piece_on_dest = board.get_case_from_coord(chk_x, chk_y).piece
                if piece_on_dest is None:
                        res.append([chk_x, chk_y])
                elif piece_on_dest.team != self.team:
                        res.append([chk_x, chk_y]) 
                        break
                else:
                    break
        
        return sorted(res)
        