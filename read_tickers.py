# 1.  read the tickers

import json
import urllib
from urllib2 import quote
import time

def read_ticker():
    fh = open('tickers')
    tickers = []
    for line in fh:
        sp = line.split()
        tickers.append(sp[0])

    # 2. form a URL to get stock data
    fn = 'ticker_test_' + time.strftime('%Y-%m-%d_%H:%M:%S')
    fp = open(fn, 'w')
    fields = ['ticker', 'PreviousClose', 'LastTradePrice', 'LastTradeTime', 'Change_PercentChange']
    fp.write(','.join(fields)+'\n')

    j = 0
    while j < len(tickers):
        sqlst = 'select * from yahoo.finance.quotes where symbol in ('
        t = ''
        if j+100 > len(tickers):
            t = '"'+'","'.join(tickers[j:])+'"'
        else:
            t = '"'+'","'.join(tickers[j:j+100])+'"'
        j += 100

        sqlst = sqlst + t + ')'
        codesql = quote(sqlst)
        tarurl = 'http://query.yahooapis.com/v1/public/yql?q=' + codesql +'&format=json&env=http://datatables.org/alltables.env'
        print 'req '+tarurl
        jsondata = json.loads(urllib.urlopen(tarurl).read())
        if 'query' not in jsondata or \
            'results' not in jsondata['query'] or \
            'quote' not in jsondata['query']['results']:
            continue
        for info in jsondata['query']['results']['quote']:
            try:
                fp.write(info.get('symbol'))
            except:
                fp.write('NULL')
            fp.write(',')
            try:
                fp.write(info.get('PreviousClose'))
            except:
                fp.write('NULL')
            fp.write(',')
            try:
                fp.write(info.get('LastTradePriceOnly'))
            except:
                fp.write('NULL')
            fp.write(',')
            try:
                fp.write(info.get('LastTradeTime'))
            except:
                fp.write('NULL')
            fp.write(',')
            try:
                fp.write(info.get('Change_PercentChange'))
            except:
                fp.write('NULL')
            fp.write('\n')
        print 'write 1 batch done.'
    fp.close()

if __name__ == '__main__':
    read_ticker()
