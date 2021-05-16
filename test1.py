from td.client import TDClient
from config import client_id,td_id,td_pwd,old15_accnt,main_accnt,ira15_accnt 
from datetime import datetime
from datetime import timedelta
import time
import pprint
from b_s_order import buy_sell_market,buy_sell_stop,buy_sell_limit
import os


cdir = os.getcwd()
tdsession = TDClient(
    client_id=client_id,
    redirect_uri='http://localhost',
    credentials_path=cdir + r'\tdameritrade.json'         
)

tdsession.login()




#data=tdsession.get_movers('$DJI','up','percent')




#tdsession.cancel_order(old15_accnt,tdsession.get_orders_query(old15_accnt))
#tdsession.place_order(main_accnt, buy_sell_limit('buy',1.15,1,'novn'))
#tdsession.place_order(main_accnt, buy_sell_stop('sell',1.00,1,'novn'))
#tdsession.place_order(main_accnt,oco_can(1.50,.90,.93))
#tdsession.place_order(old15_accnt, oco_bracket(1.14,1.29,1.05))
#pprint.pprint(tdsession.get_orders_query(old15_accnt))
quer=tdsession.get_orders_query(main_accnt)
pprint.pprint(quer)




#pprint.pprint(tdsession.get_orders_path(old15_accnt))
#pprint.pprint(tdsession.get_accounts(old15_accnt,fields=['orders','positions']))
# Define a list of all valid periods
#pos = tdsession.get_accounts(old15_accnt,fields=['orders','positions'])
#pprint.pprint(pos)
#pprint.pprint(pos['securitiesAccount']['positions'][0]['instrument']['symbol'])
# for i in range(len(pos['securitiesAccount']['positions'])):
#     pprint.pprint(pos['securitiesAccount']['positions'][i]['instrument']['symbol'])
#     print(i)#print(i)# + ' ' + i['accountId']['positions'][0]['averagePrice']['instrument'])
#tdsession.place_order(ira15_accnt,oco_bracket())
