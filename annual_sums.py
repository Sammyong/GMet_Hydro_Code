# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 01:07:24 2018

@author: Akpene
"""
#This script is to filter missing data from station data and calculate 
#the annual sum.

import pandas as pd

#Read data
rf  = pd.read_excel('C:\\Users\\hydro\Dropbox\\data\\Rainfall_1961_2016.xlsx')

#stn_name = input('Enter the station name in capitals: ')

#stns='NAVRONGO','WA','BOLE','TAMALE','YENDI','WENCHI','KETE_KRACHI',\
#'SUNYANI','KUMASI','SEFWI_BEKWAI','ABETIFI','HO','AKIM_ODA','KOFORIDUA',\
#'AKUSE','AKATSI','TAKORADI','AXIM','SALTPOND','ACCRA','TEMA','ADA',

####################################################################

#Print the entire row with some selected columns from the original data.
syr = rf[['stn', 'Year','rr']]
#print(syr)

#filter all values > -99.9 where -99.9 is the missing values
fsyr =syr[syr['rr'] > -99.9]
print(fsyr)



#index the row and column
fsyr = fsyr.set_index(['stn'])

#print the rainfall data with each year station by station and stored in salf
idx  = pd.IndexSlice
salf = fsyr.loc[idx['AKUSE'],:]

#ansum is the annual sum for each station
ansum = salf.groupby('Year').sum().reset_index()
#print(ansum)
print('Done!!!')