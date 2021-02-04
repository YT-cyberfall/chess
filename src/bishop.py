#!/usr/bin/env python
# -*- coding: utf-8 -*-

import piece


class Bishop(piece.Piece):
    
    def __init__(self, team):
        super().__init__(team)
        self.name = 'Bishop'
        self.annotation = 'B'