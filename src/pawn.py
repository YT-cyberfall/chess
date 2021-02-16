#!/usr/bin/env python
# -*- coding: utf-8 -*-

import piece


class Pawn(piece.Piece):
    '''Representing a Pawn piece
    
        Attributes :
        team : str : The team of the piece (white or black)
        name : str : The english name of the piece
        annotation : char : The piece letter for writting moves
        first_move : bool : Whether the piece has move or not
        
        Methods :
        __init__ : Create a rook piece from Piece object
        get_all_moves : Returns all the possible moves by the PAwn 
    '''
    
    
    def __init__(self, team):
        '''Create a pawn piece from Piece object
        
        Arguments : 
        team : str : wether the piece is white or black
        '''
        super().__init__(team)
        self.name = 'Pawn'
        self.annotation = 'P'
        self.first_move = True
        
        
    # TODO en passant and promotion
    def get_all_moves(self, x, y, board):
        '''Returns all the possible moves by the Pawn
        
        Arguments : 
        x : integer : the x position of the pawn on the board 
        y : integer : the y position of the pawn on the board 
        board : Board : the current board to play the move 
        
        Returns : list : containing all moves as [x_destination, y_destination]
        '''

        res = []
        team = int(self.team == 'black') # 0 if white else 1
        
        # Moving up or down depending of the team
        check = [
            [y + 1, y + 2],
            
            [y - 1, y - 2],
            
        ]
        
        # The value to go forward
        m1 = check[team][0]
        m2 = check[team][1]
        
        # Simply movinf by one or two squares depending the context
        if m1 in range(8) and board.get_case_from_coord(x, m1).piece is None:
            res.append([x, m1])
            if self.first_move and \
                board.get_case_from_coord(x, m2).piece is None:
                res.append([x, m2])
                
        # Check the capture in diagonal if possible or not
        for val in {x - 1, x + 1}:
            if all(v in range(8) for v in (val, m1)):
                piece_on_des = board.get_case_from_coord(val, m1).piece
                if piece_on_des is not None and piece_on_des.team != self.team:
                    res.append([val, m1])
                
        return sorted(res)
            
    