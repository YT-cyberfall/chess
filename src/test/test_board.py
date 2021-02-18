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
                        self.board.graveyard.get('black'))
        
        
    def test_play_a_move_classical(self):
        '''Test the board state after moving a piece capturing another'''
        
        # Ra1d4 - Rd4xg7
        self.board.play_a_move((0,0), (3,3)) 
        self.board.play_a_move((3,3), (6,6)) 
        self.assertEqual(self.board.board[0].piece, None)
        self.assertEqual(self.board.board[54].piece.team, 'white')
        self.assertEqual(self.board.board[54].piece.name, 'Rook')
        self.assertEqual(len(self.board.graveyard.get('black')), 1)
        self.assertEqual(len(self.board.graveyard.get('white')), 0)
        
        
    def test_play_a_move_exc(self):
        '''Test the exceptions with bad values gave to the function as :
        out of board, on same color moving, on same square, moving a None square
        '''
        
        self.assertRaises(ValueError, lambda : self.board.play_a_move((7,0), 
                                                                      (8,6)))
        self.assertRaises(ValueError, lambda : self.board.play_a_move((-1,0), 
                                                                      (1,6)))
        self.assertRaises(ValueError, lambda : self.board.play_a_move((1,0), 
                                                                      (1,0)))
        self.assertRaises(ValueError, lambda : self.board.play_a_move((1,0), 
                                                                      (2,0)))
        self.assertRaises(ValueError, lambda : self.board.play_a_move((4,3), 
                                                                      (2,0)))
        
        
    def test_get_move_for_square(self):
        '''Test the capturing possibilities of each pieces'''
        
        #Nb1e6
        self.board.play_a_move((1,0), (4,5))
        self.assertEqual(self.board.get_move_for_square(4, 5), sorted([
            [3,7], [5,7], [2,6], [6,6], [6,4], [2,4], [3,3], [5,3]]))
        
        #Ra1d6
        self.board.play_a_move((0,0), (3,5))
        self.assertEqual(self.board.get_move_for_square(3, 5), sorted([
            [2,5], [1,5], [0,5], [3,4], [3,3], [3,2], [3,6]]))
        
        #Bc8f3
        self.board.play_a_move((2,7), (5,2))
        self.assertEqual(self.board.get_move_for_square(5, 2), sorted([
            [4,1], [6,1], [6,3], [7,4], [4,3], [3,4], [2,5]]))
        
        #Qd1h6
        self.board.play_a_move((3,0), (7,5))
        self.assertEqual(self.board.get_move_for_square(7, 5), sorted([
            [7,6], [6,6], [6,5], [5,5], [7,4], [7,3], [7,2], [6,4], [5,3], 
            [4,2]]))
        
        #Ph2a6
        self.board.play_a_move((7,1), (0,5))
        self.assertEqual(self.board.get_move_for_square(0, 5), sorted([[1,6]]))        
        
        #Ke8c3
        self.board.play_a_move((4,7), (2,2))
        self.assertEqual(self.board.get_move_for_square(2, 2), sorted([
            [1,1], [2,1], [3,1], [1,2], [1,3], [2,3], [3,3], [3,2]]))
        
        #En passant possibilities # c7c4 b4 
        self.board.play_a_move((2,6), (2,3)) 
        self.board.play_a_move((1,1), (1,3))
        self.assertEqual(self.board.get_move_for_square(2, 3), sorted([[1,2]]))
        
        
    def test_get_case_from_coords(self):
        '''Test if the selection of a sqaure by its cooridnate is correct'''
        
        case0 = self.board.board[0]
        case1 = self.board.board[5]
        case2 = self.board.board[28]
        case3 = self.board.board[63]
        self.assertEqual(self.board.get_case_from_coord(0,0), case0)
        self.assertEqual(self.board.get_case_from_coord(5,0), case1)
        self.assertEqual(self.board.get_case_from_coord(4,3), case2)
        self.assertEqual(self.board.get_case_from_coord(7,7), case3)
        
        # Values outside the board has no points
        self.assertRaises(ValueError, 
                          lambda : self.board.get_case_from_coord(8,7))
        self.assertRaises(ValueError, 
                          lambda : self.board.get_case_from_coord(-1,7))
        
        
    def test_get_last_name(self):
        '''Test if the last move write in the ihistory is correct'''
        self.assertEqual(self.board._get_last_move(), None)
        self.board.play_a_move((1,1), (1,2))
        self.board.play_a_move((4,7), (2,2))
        self.assertEqual(self.board._get_last_move(), ' (4, 7)(2, 2)')
        self.board.play_a_move((2,7), (5,2))
        self.assertEqual(self.board._get_last_move(display_move_num=True),
                          '2. (2, 7)(5, 2)')
        
        
        
if __name__ == '__main__':
    unittest.main()