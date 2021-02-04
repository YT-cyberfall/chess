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
        self.assertEqual(len(self.board.board), 64)
        self.assertEqual(len(self.board.graveyard), 2)
        self.assertFalse(self.board.graveyard.get('white') or \
            self.board.graveyard.get('black') )
        
        
if __name__ == '__main__':
    unittest.main()