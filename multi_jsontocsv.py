#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import time
import os
from functools import reduce
import pandas as pd
import glog

##open files
#j_aapl = open("/Users/manshan/Documents/data/AAPL.json")
#data_aapl = json.load(j_aapl)
#j_fb = open("/Users/manshan/Documents/data/fb.json")
#data_fb = json.load(j_fb)
##timestamp conversion
#convert = lambda x: time.strftime("%Y-%m-%d", time.localtime(x))
#d_aapl = list(map(convert, data_aapl['chart']['result'][0]['timestamp']))
#d_fb = list(map(convert, data_fb['chart']['result'][0]['timestamp']))
##price conversion
#convert2 = lambda x: '{:.2f}'.format(x)
#z_aapl = zip(d_aapl, list(map(convert2, data_aapl['chart']['result'][0]['indicators']['quote'][0]['open'])), list(map(convert2, data_aapl['chart']['result'][0]['indicators']['quote'][0]['close'])), list(map(convert2, data_aapl['chart']['result'][0]['indicators']['quote'][0]['low'])), list(map(convert2, data_aapl['chart']['result'][0]['indicators']['quote'][0]['high'])), data_aapl['chart']['result'][0]['indicators']['quote'][0]['volume'])
#z_fb = zip(d_fb, list(map(convert2, data_fb['chart']['result'][0]['indicators']['quote'][0]['open'])), list(map(convert2, data_fb['chart']['result'][0]['indicators']['quote'][0]['close'])), list(map(convert2, data_fb['chart']['result'][0]['indicators']['quote'][0]['low'])), list(map(convert2, data_fb['chart']['result'][0]['indicators']['quote'][0]['high'])), data_fb['chart']['result'][0]['indicators']['quote'][0]['volume'])
##pandas join
#left = pd.DataFrame(z_aapl, columns = ['Date', 'AAPL_Open', 'AAPL_Close', 'AAPL_Low', 'AAPL_High', 'AAPL_Volume'])
#right = pd.DataFrame(z_fb, columns = ['Date', 'FB_Open', 'FB_Close', 'FB_Low', 'FB_High', 'FB_Volume'])
#result = pd.merge(left, right, on= ['Date'], how = 'outer')
##null to zero
#import numpy as np
#result = result.replace(np.nan, 0)
##export
#result.to_csv("/Users/manshan/Documents/testdata.csv", index = False)
#
##multi
#import os
#path = "/Users/manshan/Documents/data"
#files= os.listdir(path)
#resut = {}
#for file in files: #遍历文件夹
#     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
#          f = open(path+"/"+file); #打开文件
#          symbol, df = file_to_dataframe(f)
#          result[symbol] = df
#
#          iter_f = iter(f); #创建迭代器
#          str = ""
#          for line in iter_f: #遍历文件，一行行遍历，读取文本
#              str = str + line
#          s.append(str) #每个文件的文本存到list中


#TODO.1: Complete the logic for all files (and the final join).
#TODO.2: Define a class for all the processing logics.
def file_to_dataframe(fp):
    data = json.load(fp)
    symbol = data['chart']['result'][0]['meta']['symbol']
    #date format
    convert = lambda x: time.strftime("%Y-%m-%d", time.localtime(x))
    d = list(map(convert, data['chart']['result'][0]['timestamp']))
    #price conversion
    convert2 = lambda x: '{:.2f}'.format(x)
    quote = data['chart']['result'][0]['indicators']['quote'][0]
    # glog.info(quote['open'])
    df = None
    try:
        z = zip(d, list(map(convert2, quote['open'])),
                list(map(convert2, quote['close'])),
                list(map(convert2, quote['low'])),
                list(map(convert2, quote['high'])), quote['volume'])

        df = pd.DataFrame(z,
                          columns=[
                              'Date', symbol + '_Open', symbol + '_Close',
                              symbol + '_Low', symbol + '_High',
                              symbol + '_Volume'
                          ])
    except:
        pass
    return symbol, df


# {
#     'AAPL': pd.DataFrame(),
#     'FB': pd:DataFrame(),
# }


class Converter:
    def __init__(self):
        self.data = {}
        self.negcount = 0
        self.poscount = 0
    # self.symbol = symbol
    # self.df = df

    def consume(self, fname):
        # read in 1 file, convert to df, saved in self.XXX
        data = json.load(fname)
        symbol = data['chart']['result'][0]['meta']['symbol']
        # date format
        convert = lambda x: time.strftime("%Y-%m-%d", time.localtime(x))
        d = list(map(convert, data['chart']['result'][0]['timestamp']))
        #price conversion
        convert2 = lambda x: '{:.2f}'.format(x)
        quote = data['chart']['result'][0]['indicators']['quote'][0]
        # glog.info(quote['open'])
        df = None
        try:
            z = zip(d, list(map(convert2, quote['open'])),
                    list(map(convert2, quote['close'])),
                    list(map(convert2, quote['low'])),
                    list(map(convert2, quote['high'])), quote['volume'])
            df = pd.DataFrame(z,
                              columns=[
                                  'Date', symbol + '_Open', symbol + '_Close',
                                  symbol + '_Low', symbol + '_High',
                                  symbol + '_Volume'
                              ])
            self.data[symbol] = df
            for i in range(1, len(df)):
                glog.info('i = {}'.format(i))
                glog.info(symbol+'_Close')
                glog.info(df.loc[i, symbol + '_Close'], df.loc[i-1, symbol + '_Close'], type(float(df.loc[i, symbol + '_Close'])))
                glog.info(float(df.loc[i, symbol + '_Close']) - float(df.loc[i-1, symbol + '_Close']))
                if float(df.loc[i, symbol + '_Close']) - float(df.loc[i-1, symbol + '_Close']) > 0: 
                    glog.info('poscount is {}'.format(self.poscount))
                    self.poscount += 1
                if float(df.loc[i, symbol + '_Close']) - float(df.loc[i-1, symbol + '_Close']) < 0: 
                    glog.info('negcount is {}'.format(self.negcount))
                    self.negcount += 1
                
        except Exception as e:
            print(e)

    def produce(self):
        # do join
        dfs = list(self.data.values())
        df_merged = reduce(
            lambda left, right: pd.merge(left, right, on=['Date'], how='outer'
                                         ), dfs).fillna('0')
        df_merged.to_csv("/Users/manshan/Documents/testdata.csv", index=False)


if __name__ == '__main__':
    path = "/Users/manshan/Documents/testdata"
    files = os.listdir(path)
    converter = Converter()
    for fname in files:
        glog.info('Now we are reading from {}'.format(fname))
        fp = open(path + "/" + fname)
        # symbol, df = file_to_dataframe(fp)
        converter.consume(fp)
    converter.produce()
    glog.info('poscount total is {}'.format(converter.poscount))
    glog.info('negcount total is {}'.format(converter.negcount))

    # converter = Converter()
    # for fname in files:
    #     converter.consume(fname)
    # return converter.produce()
