# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:04:21 2021

@author: chyng
"""

#algorithm description: https://nrich.maths.org/1443

players = ['raphael', 'michelangelo', 'donatello', 'leonardo']
#players = ['7', '1', '2', '3', '4', '5', '6', '8']


def split_list(my_list):
    half = len(my_list)//2
    return my_list[:half], my_list[half:]

def final_pairs_from_even(my_list):
    final_pairs = []
    for j in range(len(my_list)-1):
        
        players_1, players_2 = split_list(my_list)
        
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
        
        my_list.insert(0, my_list.pop(players.index(my_list[-2])))
        
    return final_pairs




def final_pairs_from_odd(my_list):
    final_pairs = []
    for j in range(len(my_list)):
        
        players_1, players_2 = split_list(my_list)
        players_2 = players_2[1:]
        players_2.reverse()
        
        #print(list, players_1, players_2)
        
        pairs = []
        
        for i in range(len(players_1)):
            pairs.append(players_1[i] + " - " + players_2[i])
        #print(pairs)
        
        final_pairs.append(pairs)
        
        my_list.insert(0, my_list.pop())
        
    return final_pairs



if (len(players) % 2) == 0:
    print(final_pairs_from_even(players))
else:
    print(final_pairs_from_odd(players))

