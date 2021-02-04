#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
test_case.py
------------
'''
import sys
sys.path.append('src/')

import unittest
import case 
import rook, knight, bishop, queen, king, pawn


class TestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        # the pieces_position.config object's got the initial position
        with open('datas/pieces_position.config', 'r') as f:
            self.pieces_positions = eval(f.read())
    
    @classmethod
    def setUp(self):
        self.case1 = case.Case(1, self.pieces_positions)
        self.case2 = case.Case(5, self.pieces_positions)
        self.case3 = case.Case(29, self.pieces_positions)
        
    
    def test_init(self):
        self.assertTrue(isinstance(self.case1.piece, knight.Knight))
        self.assertEqual((self.case1.x, self.case1.y), (1, 0))
        self.assertEqual(self.case1.color, 'white')
        
        self.assertTrue(isinstance(self.case2.piece, bishop.Bishop))
        self.assertEqual((self.case2.x, self.case2.y), (5, 0))
        self.assertEqual(self.case2.color, 'white')
        
        
        self.assertIsNone(self.case3.piece)
        self.assertEqual((self.case3.x, self.case3.y), (5, 3))
        self.assertEqual(self.case3.color, 'black')
        

if __name__ == '__main__':
    unittest.main()
        