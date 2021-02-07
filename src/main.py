#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import board


b = board.Board()
b.pprint()

b.play_a_move((1,0), (6,6))
b.pprint()

# TODO PEP8fy
# TODO defining step to go throught
# For each step trying to define fucntions, and then write test
# TODO add a requirement.txt

