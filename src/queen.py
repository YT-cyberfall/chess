#!/usr/bin/env python
# -*- coding: utf-8 -*-

import piece


class Queen(piece.Piece):
    
    def __init__(self, team):
        super().__init__(team)
        self.name = 'Queen'
        self.annotation = 'Q'