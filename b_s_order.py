from td.client import TDClient
from config import client_id,td_id,td_pwd,old15_accnt,main_accnt 
import time
import pprint

def buy_sell_market(bs,qty,tiker)->dict():
    if bs == 'buy'.lower():  
      bs = 'Buy'
    elif bs == 'sell'.lower():
      bs = 'Sell'
    else:
      return None
    order={
  "orderType": "MARKET",
  "session": "NORMAL",
  "duration": "DAY",
  "orderStrategyType": "SINGLE",
  "orderLegCollection": [
    {
      "instruction": bs,
      "quantity": float(qty),
      "instrument": {
        "symbol": tiker,
        "assetType": "EQUITY"
      }
    }
  ]
}
    return (order)






def buy_sell_stop(bs,stp_price,qty,tiker)->dict():
    if bs == 'buy'.lower():  
      bs = 'Buy'
    elif bs == 'sell'.lower():
      bs = 'Sell'
    else:
      return "No Orders"
    ocot = {
      #//REPRESENTS A STOP MARKET ORDER FOR BUYING A POSITION I ALREADY DON'T OWN. STOP PRICE MUST BE ABOVE THE CURRENT MARKET PRICE.
      "orderType": "STOP",
      "session": "NORMAL",
      "duration": "DAY",
      "stopPrice": float(stp_price),
      "orderStrategyType": "SINGLE",
      "orderLegCollection": [
        {
          "instruction": bs,
          "quantity": float(qty),
          "instrument": {
            "symbol": tiker,
            "assetType": "EQUITY"
          }
        }
      ]
    }
    return ocot




def buy_sell_limit(bs,lmitprice,qty,tiker)->dict():
    if bs == 'buy'.lower():  
      bs = 'Buy'
    elif bs == 'sell'.lower():
      bs = 'Sell'
    else:
      return "No Orders"
    ocot = {
      #//REPRESENTS A STOP MARKET ORDER FOR BUYING A POSITION I ALREADY DON'T OWN. STOP PRICE MUST BE ABOVE THE CURRENT MARKET PRICE.
      "orderType": "LIMIT",
      "session": "SEAMLESS",
      "duration": "DAY",
      "price": float(lmitprice),
      "orderStrategyType": "SINGLE",
      "orderLegCollection": [
        {
          "instruction": bs,
          "quantity": float(qty),
          "instrument": {
            "symbol": tiker,
            "assetType": "EQUITY"
          }
        }
      ]
    }
    return ocot
