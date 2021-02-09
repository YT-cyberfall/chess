#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import board


b = board.Board()
b.play_a_move((0,0),(3,5))
v = b.get_move_for_square(3,5)
print(v)
# TODO PEP8fy
# For each step trying to define fucntions, and then write test
# TODO add a requirement.txt

