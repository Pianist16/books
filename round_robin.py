# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:04:21 2021

@author: chyng
"""

#algorithm description: https://nrich.maths.org/1443

#players = ['raphael', 'michelangelo', 'donatello', 'leonardo']
players = ['7', '1', '2', '3', '4', '5', '6', '8']


def split_list(list):
    half = len(list)//2
    return list[:half], list[half:]

def final_pairs_from_even(list):
    final_pairs = []
    for j in range(len(list)-1):
        
        players_1, players_2 = split_list(list)
        
        # first pair
        pairs = [players_1[-1] + " - " + players_2[-1]]
        
            
        # remove the first pair
        players_1 = players_1[:-1]
        players_2 = players_2[:-1]
        players_2.reverse()
        
        for i in range(len(players_1)):
            pairs.append(players_1[i] + " - " + players_2[i])
        #print(pairs)
        
        final_pairs.append(pairs)
        
        list.insert(0, list.pop(players.index(list[-2])))
        
    return final_pairs




def final_pairs_from_odd(list):
    final_pairs = []
    for j in range(len(list)):
        
        players_1, players_2 = split_list(list)
        players_2 = players_2[1:]
        players_2.reverse()
        
        #print(list, players_1, players_2)
        
        pairs = []
        
        for i in range(len(players_1)):
            pairs.append(players_1[i] + " - " + players_2[i])
        #print(pairs)
        
        final_pairs.append(pairs)
        
        list.insert(0, list.pop())
        
    return final_pairs



if (len(players) % 2) == 0:
    print(final_pairs_from_even(players))
else:
    print(final_pairs_from_odd(players))

