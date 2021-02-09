#!/usr/bin/env python
# -*- coding: utf-8 -*-

import piece


class Rook(piece.Piece):
    
    def __init__(self, team):
        super().__init__(team)
        self.name = 'Rook'
        self.annotation = 'R'
    
    
    def get_all_moves(self, x, y, board):
        '''return all the moves possible on an empty board'''
        res = []
        eat = False
        
        
        
        # for x_2 in [i for i in range(8)]:
            # for y_2 in [i for i in range(8)]:
                # print(x_2, y_2)
                # if (x_2 != x or y_2 != y) and (y_2 == y or x_2==x) :
                    # print('\t' , x_2, y_2)
                    # 
                    # if board.get_case_from_coord(x_2, y_2).piece is None:
                        # res.append([x_2, y_2])
                    # elif board.get_case_from_coord(x_2, y_2).piece.team != self.team and eat == False:
                        # res.append([x_2, y_2])    
                    # else:
                        # break
                    # 
                    
                    
            #l'idée et de parcourir de droite a gauche, en faisnt les 4 cpte"
            #gauche
        for x2 in range(x):
            if board.get_case_from_coord(x2, y).piece is None:
                    res.append([x2, y])
            elif board.get_case_from_coord(x2, y).piece.team != self.team and eat == False:
                    res.append([x2, y]) 
                    eat = True
            else:
                break
        eat = False
        #droite
        for x2 in range(x+1, 8):
            
            if board.get_case_from_coord(x2, y).piece is None:
                    res.append([x2, y])
            elif board.get_case_from_coord(x2, y).piece.team != self.team and eat == False:
                    res.append([x2, y]) 
                    eat = True
            else:
                break
        eat = False
        
        #haut
        for y2 in range(y)[::-1]:
            print(y2)
            
            if board.get_case_from_coord(x, y2).piece is None:
                    res.append([x, y2])
            elif board.get_case_from_coord(x, y2).piece.team != self.team and eat == False:
                    res.append([x, y2]) 
                    eat = True
            else:
                eat = False
                break
        #base
        eat = False
        
        for y2 in range(y+1, 8):
            if board.get_case_from_coord(x, y2).piece is None:
                res.append([x, y2])
            elif board.get_case_from_coord(x, y2).piece.team != self.team and eat == False:
                    res.append([x, y2]) 
                    eat = True
            else:
                eat = False
                break

        return sorted(res)
        