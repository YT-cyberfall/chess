#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Piece:
    
    def __init__(self, team):
        self.team = team
        
    def __str__(self):
        ''' Overloading print function
        Returns the current instance as : 
        attr1 => value
        attr2 => value
        ....
        '''
        return '\n'.join([f'{a} => {getattr(self, a)} ' for a in dir(self) \
            if not a.startswith('__')])
        