#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import board


b = board.Board()
print(b.pprint())

b.play_a_move((1,1), (1,4))
print(b.pprint())

b.play_a_move((0,6), (0,4))
c = b.get_case_from_coord(1, 4) # 1,4 - 0-5, 2-5
print(b.pprint())

c.piece.get_all_moves(1, 4, b)


