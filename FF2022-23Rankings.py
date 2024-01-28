#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 19:44:01 2022

@author: jimmywhalen
"""

import pandas as pd

df = pd.read_excel('/Users/jimmywhalen/Desktop/Python/FF2022-23.xlsx')



scoring = {
    'receptions': 1,
    'yds': .1,
    'tds': 6,
    'pass_yds': .04,
    'pass_tds': 4,
    'int': -2
    }

df['FantasyPoints'] = (df['Rec']*scoring['receptions']+df['Combined Yds']*scoring['yds']+df['Combined TDs']*scoring['tds']+df['Passing Yds']*scoring['pass_yds']+df['Passing TDs']*scoring['pass_tds']+df['Ints']*scoring['int'])
# ^ adding a variable

df.FantasyPoints = df.FantasyPoints.round(2)

df['Rank'] = df['FantasyPoints'].rank(ascending = False)
df = df.sort_values('Rank')
# print(df[100:120])


adp_df = pd.read_csv('https://raw.githubusercontent.com/VTNoble/adp-vs-projection/main/2022-07-27/data/adp.csv')
adp_df = adp_df.drop(columns=['Date', 'Redraft SF ADP', 'Dynasty PPR ADP', 'Dynasty Half PPR ADP', 'Dynasty SF ADP', 'IDP ADP', 'Player Team', 'Player Id', 'Positional Rank'])
adp_df['ADP Rank'] = adp_df['Redraft PPR ADP'].rank()
adp_df = adp_df.sort_values('ADP Rank')
adp_df = adp_df.drop(columns=['Redraft PPR ADP', 'Redraft Half PPR ADP'])
# print(adp_df[120:130])

# adp_df.shape
adp_df_cutoff1 = adp_df[:75]
adp_df_cutoff2 = adp_df[:99]
adp_df_cutoff3 = adp_df[:125]
adp_df_cutoff4 = adp_df[:150]


# adp_df_cutoff.head(100)

replacement_players1 = {  
    'RB': '',
    'WR': '',
    'QB': '',
    'TE': '',
}
replacement_players2 = {  
    'RB': '',
    'WR': '',
    'QB': '',
    'TE': '',
}
replacement_players3 = {  
    'RB': '',
    'WR': '',
    'QB': '',
    'TE': '',
}
replacement_players4 = {  
    'RB': '',
    'WR': '',
    'QB': '',
    'TE': '',
}

for _, row in adp_df_cutoff1.iterrows():
    position = row['Fantasy Player Positions']
    first_player = row['Player First Name']
    last_player = row['Player Last Name']
    player_name = first_player + ' ' + last_player
    
    if position in replacement_players1:
      replacement_players1[position] = player_name
      
for _, row in adp_df_cutoff2.iterrows():
    position = row['Fantasy Player Positions']
    first_player = row['Player First Name']
    last_player = row['Player Last Name']
    player_name = first_player + ' ' + last_player
    
    if position in replacement_players2:
      replacement_players2[position] = player_name
    
for _, row in adp_df_cutoff3.iterrows():
    position = row['Fantasy Player Positions']
    first_player = row['Player First Name']
    last_player = row['Player Last Name']
    player_name = first_player + ' ' + last_player
    
    if position in replacement_players3:
      replacement_players3[position] = player_name
    
for _, row in adp_df_cutoff4.iterrows():
    position = row['Fantasy Player Positions']
    first_player = row['Player First Name']
    last_player = row['Player Last Name']
    player_name = first_player + ' ' + last_player
    
    if position in replacement_players4:
      replacement_players4[position] = player_name
    
# print(replacement_players1)
# print(replacement_players2)
# print(replacement_players3)
# print(replacement_players4)

# qb_df = df.loc[(df['Pos'] == 'QB')]
# qb_df = qb_df[['Pos', 'Name', 'FantasyPoints']]
# qb_df['Rank'] = qb_df['FantasyPoints'].rank(ascending = False)
# print(qb_df.sort_values('Rank'))

# rb_df = df.loc[(df['Pos'] == 'RB')]
# rb_df = rb_df[['Pos', 'Name', 'FantasyPoints']]
# rb_df['Rank'] = rb_df['FantasyPoints'].rank(ascending = False)
# print(rb_df.sort_values('Rank'))

# wr_df = df.loc[(df['Pos'] == 'WR')]
# wr_df = wr_df[['Pos', 'Name', 'FantasyPoints']]
# wr_df['Rank'] = wr_df['FantasyPoints'].rank(ascending = False)
# print(wr_df.sort_values('Rank'))

# te_df = df.loc[(df['Pos'] == 'TE')]
# te_df = te_df[['Pos', 'Name', 'FantasyPoints']]
# te_df['Rank'] = te_df['FantasyPoints'].rank(ascending = False)
# print(te_df.sort_values('Rank'))

# replacement_values1 = {
#     'RB': '',
#     'WR': '',
#     'QB': '',
#     'TE': '',
#     }
# replacement_values2 = {
#     'RB': '',
#     'WR': '',
#     'QB': '',
#     'TE': '',
#     }
# replacement_values3 = {
#     'RB': '',
#     'WR': '',
#     'QB': '',
#     'TE': '',
#     }
# replacement_values4 = {
#     'RB': '',
#     'WR': '',
#     'QB': '',
#     'TE': '',
#     }


# for position, player_name in replacement_players1.items():
#     player = df.loc[df['Name'] == player_name]
#     replacement_values1[position] = player['FantasyPoints'].tolist()
    
# for position, player_name in replacement_players2.items():
#     player = df.loc[df['Name'] == player_name]
#     replacement_values2[position] = player['FantasyPoints'].tolist()

# for position, player_name in replacement_players3.items():
#     player = df.loc[df['Name'] == player_name]
#     replacement_values3[position] = player['FantasyPoints'].tolist()

# for position, player_name in replacement_players4.items():
#     player = df.loc[df['Name'] == player_name]
#     replacement_values4[position] = player['FantasyPoints'].tolist()

# print(replacement_values1)
# print(replacement_values2)
# print(replacement_values3)
# print(replacement_values4)


# *********Average of all replacement values *****

# combo = {
#     'RB': '',
#     'WR': '',
#     'QB': '',
#     'TE': '',
#     }

# values_df = pd.Dataframe([replacement_values1, replacement_values2, replacement_values3, replacement_values4])
# answer = dict(values_df.mean())
# print(values_df)


# from collections import Counter

# sums = Counter()
# counters = Counter()
# for itemset in [replacement_values1, replacement_values2, replacement_values3, replacement_values4]:
#     sums.update(itemset)
#     counters.update(itemset.keys())
    
# ret = {lambda x: float(sums[x]/counters[x] for x in sums.keys())}
# print(ret)



rb_df = df.loc[(df['Pos'] == 'RB')]
rb_df = rb_df[['Pos', 'Name', 'FantasyPoints']]
rb_df['Pos Rank'] = rb_df['FantasyPoints'].rank(ascending = False)
rb_df['VOR'] = rb_df.apply(lambda row: row['FantasyPoints'] - 137.7, axis=1)
#122.8 for 0.5 PPR
# 137.7 for PPR

wr_df = df.loc[(df['Pos'] == 'WR')]
wr_df = wr_df[['Pos', 'Name', 'FantasyPoints']]
wr_df['Pos Rank'] = wr_df['FantasyPoints'].rank(ascending = False)
wr_df['VOR'] = wr_df.apply(lambda row: row['FantasyPoints'] - 170.4, axis=1)
# 135.7 for 0.5 PPR
# 170.4 for PPR

qb_df = df.loc[(df['Pos'] == 'QB')]
qb_df = qb_df[['Pos', 'Name', 'FantasyPoints']]
qb_df['Pos Rank'] = qb_df['FantasyPoints'].rank(ascending = False)
qb_df['VOR'] = qb_df.apply(lambda row: row['FantasyPoints'] - 298.1, axis=1)
# 352.1 for 6 point TDs
# 298.1 for 4 point TDs

te_df = df.loc[(df['Pos'] == 'TE')]
te_df = te_df[['Pos', 'Name', 'FantasyPoints']]
te_df['Pos Rank'] = te_df['FantasyPoints'].rank(ascending = False)
te_df['VOR'] = te_df.apply(lambda row: row['FantasyPoints'] - 150.7, axis=1)
# 120.7 for 0.5 PPR
#150.7 for PPR

frames = [rb_df, wr_df, qb_df, te_df]
result = pd.concat(frames)
ndf = result.sort_values('VOR', ascending=False)
ndf['Rank'] = ndf['VOR'].rank(ascending=False)
print(ndf.head(60))

# ndf.to_excel('/Users/jimmywhalen/Desktop/Python/VOR Sheet.xlsx', sheet_name = 'Total')
# with pd.ExcelWriter('VOR Sheet.xlsx') as writer: 
#     ndf.to_excel('/Users/jimmywhalen/Desktop/Python/VOR Sheet.xlsx', sheet_name = 'Total')
#     qb_df.to_excel('/Users/jimmywhalen/Desktop/Python/VOR Sheet.xlsx', sheet_name = 'QB')
#     rb_df.to_excel('/Users/jimmywhalen/Desktop/Python/VOR Sheet.xlsx', sheet_name = 'RB')
#     wr_df.to_excel('/Users/jimmywhalen/Desktop/Python/VOR Sheet.xlsx', sheet_name = 'WR')
#     te_df.to_excel('/Users/jimmywhalen/Desktop/Python/VOR Sheet.xlsx', sheet_name = 'TE')

# players at 100: Penny, Olave, Stafford, Knox
# at 75: Walker, Smith-Schuster, Hurts, Schultz
# at 50: Dobbins, Moore, Jackson, Waller

