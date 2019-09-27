#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 19:08:35 2019

@author: Ronnit
"""

import pandas as pd

df = pd.read_csv('Path to File containing drive links')

data1 = ('Google Drive File - Shareable Link')
da1 = data1.split('https://drive.google.com/open?id=')[-1]
final_link1 = 'https://www.googleapis.com/drive/v3/files/'+da1+'?alt=media&key=AIzaSyDGM7x8fm19WaGevPLCBVGLNy3zLhpBdds'

#This is to obtain only the id of the file for sharing
dl = df['Drive Link'].apply(lambda x: x.split('https://drive.google.com/open?id=')[-1])

final_link = 'https://www.googleapis.com/drive/v3/files/'+dl+'?alt=media&key=AIzaSyDGM7x8fm19WaGevPLCBVGLNy3zLhpBdds'

final_link.to_csv('Final_File.csv')