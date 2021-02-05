#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
test_board.py
------------
'''
import sys
sys.path.append('src/')

import unittest
import board 

class TestBoard(unittest.TestCase):
    
    @classmethod
    def setUp(self):
        self.board = board.Board()
        
    def test_init(self):
        '''Test the board initialization'''
        self.assertEqual(len(self.board.board), 64)
        self.assertEqual(len(self.board.graveyard), 2)
        self.assertFalse(self.board.graveyard.get('white') or \
            self.board.graveyard.get('black') )
        
    def test_play_a_move_classical(self):
        '''Test the board state after moving a piece capturing another'''
        
        # Ra1-d4 - Rd4xg7
        self.board.play_a_move((0,0), (3,3))
        self.board.play_a_move((3,3), (6,6))
        self.assertEqual(self.board.board[0].piece, None)
        self.assertEqual(self.board.board[54].piece.team, 'white')
        self.assertEqual(self.board.board[54].piece.name, 'Rook')
        self.assertEqual(len(self.board.graveyard.get('black')), 1)
        self.assertEqual(len(self.board.graveyard.get('white')), 1)
        
    def test_play_a_move_exc(self):
        '''Test the exceptions with bad values gave to the function as :
        out of board, on same color moving, on same square'''
        
        self.assertRaises(ValueError, lambda : self.board.play_a_move((7,0), (8,6)))
        self.assertRaises(ValueError, lambda : self.board.play_a_move((-1,0), (1,6)))
        self.assertRaises(ValueError, lambda : self.board.play_a_move((1,0), (1,0)))
        self.assertRaises(ValueError, lambda : self.board.play_a_move((1,0), (2,0)))
        
if __name__ == '__main__':
    unittest.main()