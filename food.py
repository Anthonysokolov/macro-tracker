#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Macro Tracker Food Info
"""

food_dicts = []
keys = ['name','carbs','protein','fat']

omelette = ['omelette',0,6,5]
bar = ['meal bar', 31, 20, 12]
proteinshake = ['protein shake', 5, 20, 2]

foods = [omelette, bar, proteinshake]

for food in foods:
    food_dict = {}
    for key, value in zip(keys, food):
        food_dict[key] = value
    food_dicts.append(food_dict)
    
