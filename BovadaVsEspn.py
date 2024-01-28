#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 18:10:44 2022

@author: jimmywhalen
"""

import pandas as pd

df = pd.read_excel('/Users/jimmywhalen/Desktop/Python/BovadaVsEspn.xlsx')



scoring = {
    'receptions': 0.5,
    'yds': .1,
    'tds': 6,
    'pass_yds': .04,
    'pass_tds': 6,
    'int': -2
    }

df = df.fillna(0)

df['Bovada Fantasy Points'] = (df['Rec']*scoring['receptions']+df['Combined Yds']*scoring['yds']+df['Combined TDs']*scoring['tds']+df['Passing Yds']*scoring['pass_yds']+df['Passing TDs']*scoring['pass_tds']+df['Ints']*scoring['int'])
df['ESPN Fantasy Points'] = (df['E-Rec']*scoring['receptions']+df['ECombined Yds']*scoring['yds']+df['ECombined TDs']*scoring['tds']+df['EPassing Yds']*scoring['pass_yds']+df['EPassing TDs']*scoring['pass_tds']+df['EInts']*scoring['int'])
df['Difference'] = df['Bovada Fantasy Points'] - df['ESPN Fantasy Points']
df = df[['Pos', 'Name', 'Difference']]

df['Rank'] = df['Difference'].rank(ascending=False)
df = df.sort_values('Rank')

# pos_df = df.loc[(df['Pos'] == 'QB')]
# pos_df['Rank'] = pos_df['Difference'].rank(ascending=False)

# pos_df = pos_df.sort_values('Rank')

print(df.head(60))
# print(pos_df.head(50))