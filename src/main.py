#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import board


b = board.Board()
b.play_a_move((0,0), (3,5))
b.play_a_move((1,0), (4,5))

b.play_a_move((2,7), (5,2))
b.play_a_move((3,0), (7,5))
b.play_a_move((7,1), (0,5))

v = b.get_move_for_square(0,3)
print(b.history)


