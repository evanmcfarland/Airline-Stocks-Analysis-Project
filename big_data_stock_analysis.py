# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:17:48 2020

@author: Evan McFarland
"""

# From independant research I put together a list of all the Big Data based 
# stock companies that have similar buisiness models and meet this criteria
# We Will call this dataset data_stocks
# Data from "big_data_stocks.csv" was collected 03/09/2020


from csv import reader
opened_file = open('big_data_stocks.csv')
read_file = reader(opened_file)
data_stocks = list(read_file)
data_stocks_header = data_stocks[0]
data_stocks = (data_stocks[1:])

# Data included for each company is as follows in the given order: Ticker, 
# Share Price, Market Cap, Trailing P/E, forward P/E, PEG, P/S, P/B, EV/R, EV/EBITDA
# All ratios are calculated on an anual basis, usually trailing twelve months (ttm)

# Since the dataset is incomplete the first step is to remove bad rows
# Rows with indexes 2 and 6 have '?' and 'N/A' so they will not be included 
# in this analysis

del(data_stocks[2])
del(data_stocks[5])


# data =  data[4:,3:]
# data = data[:7,:13]

# Were now going to compute the averages of each column because they will be
# the metric that each company gets compared against

# import statistics

# x = statistics.mean(data_stocks[0])
# print(x)
