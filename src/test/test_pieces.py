#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('src/')
import unittest
import rook, knight, bishop, queen, king, pawn, piece

class TestPieces(unittest.TestCase):
    
    def test_piece_init(self):
        p = piece.Piece('white')
        self.assertEqual(p.team, 'white')
        
    def test_rook_init(self):
        p = rook.Rook('black')
        self.assertEqual(p.team, 'black')
        self.assertEqual(p.annotation, 'R')
        self.assertEqual(p.name, 'Rook')
        
    def test_knight_init(self):
        p = knight.Knight('black')
        self.assertEqual(p.team, 'black')
        self.assertEqual(p.annotation, 'N')
        self.assertEqual(p.name, 'Knight')
        
    def test_bishop_init(self):
        p = bishop.Bishop('black')
        self.assertEqual(p.team, 'black')
        self.assertEqual(p.annotation, 'B')
        self.assertEqual(p.name, 'Bishop')
        
    def test_queen_init(self):
        p = queen.Queen('black')
        self.assertEqual(p.team, 'black')
        self.assertEqual(p.annotation, 'Q')
        self.assertEqual(p.name, 'Queen')
        
    def test_king_init(self):
        p = king.King('white')
        self.assertEqual(p.team, 'white')
        self.assertEqual(p.annotation, 'K')
        self.assertEqual(p.name, 'King')
        
    def test_pawn_init(self):
        p = pawn.Pawn('white')
        self.assertEqual(p.team, 'white')
        self.assertEqual(p.annotation, 'P')
        self.assertEqual(p.name, 'Pawn')
        
    
        
