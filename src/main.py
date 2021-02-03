#!/usr/bin/env python
# -*- coding: utf-8 -*-

import board

b = board.Board()
for c in b.board:
    print(f'{chr(65 + c.x)} {c.y} - {c.color} : {c.piece}')
    
# TODO replaced by a pprint
# TODO write tests

