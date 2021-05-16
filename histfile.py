from td.client import TDClient
from config import client_id,td_id,td_pwd,old15_accnt,main_accnt,ira15_accnt 
from datetime import datetime
from datetime import timedelta
import time
import pprint
from b_s_order import buy_sell_market,buy_sell_stop,oco_bracket
import os
import sys
from conv_epoch import strt,end
import pandas as pd

cdi = os.getcwd()
if sys.platform == 'darwin':
    cdir = cdi + r'/tdameritrade.json'
    print(cdir)
elif sys.platform == 'win32':
    cdir = cdi + r'\tdameritrade.json'
    print(cdir)




tdsession = TDClient(
    client_id=client_id,
    redirect_uri='http://localhost',
    credentials_path=cdir      
)

tdsession.login()

print(strt(2017,1,1))
print(end())

#hist_amd=tdsession.get_price_history('AMD','day','5',None,None,'minute','30')

df=pd.read_csv('hist_amd45.csv',index_col=0)


print(df)
#df.to_csv('hist_amd45.csv',index=False)
