from td.client import TDClient
from config import client_id,td_id,td_pwd,old15_accnt,main_accnt,ira15_accnt 
from datetime import datetime
from datetime import timedelta
import datetime
import time
import pprint
from b_s_order import buy_sell_market,buy_sell_stop,oco_bracket
import os
import sys





cdi = os.getcwd()
if sys.platform == 'darwin':
    cdir = cdi + r'/tdameritrade.json'
    print(cdir)
elif sys.platform == 'win32':
    cdir = cdi + r'\tdameritrade.json'
    print(cdir)




print(sys.platform)
tdsession = TDClient(
    client_id=client_id,
    redirect_uri='http://localhost',
    credentials_path=cdir         
)


tdsession.login()

his_30min = tdsession.get_price_history('AMD','day',None,'1609488000000','1615756661000','minute','30' )
#print(len(his_30min))
for i in range(len(his_30min['candles'])):
    if i <= 1500:
        continue
    else:
        if his_30min['candles'][i-1]['high'] - his_30min['candles'][i-1]['low'] > his_30min['candles'][i]['high'] - his_30min['candles'][i]['low']:
            print(f"{his_30min['candles'][i-1]['high'] - his_30min['candles'][i-1]['low']}  {his_30min['candles'][i]['high'] - his_30min['candles'][i]['low']}")
            
            #print('yes')
        else:
            
            print('no')
        # close = his_30min['candles'][i]['close']
        # epch = his_30min['candles'][i]['datetime']
        # date = datetime.datetime.fromtimestamp(int(epch/1000))
        # print(f'{date}  {close}  {candle_size}')
        # time.sleep(.5)

#pprint.pprint(his_30min)
# epoch_time = 1615758411
# datetime_time = datetime.datetime.fromtimestamp(epoch_time)
# print(datetime_time)
print(len(his_30min['candles']))


def candle_size(candle_pos):
    
    for r in range(5,-2,-1):
        old_candle=his_30min['candles'][i-r]['high'] - his_30min['candles'][i-r]['low']
        pass_candle=his_30min['candles'][1]['high'] - his_30min['candles'][1]['low']
        if pass_candle > old_candle:
            cntr += 1

    