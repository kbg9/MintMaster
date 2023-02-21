from pya3 import *
from pprint import pprint
import math
import numpy as np
import time
import datetime as datetime
import pandas as pd

uid = 'xxxxxx'
key = 'xxxxxxxxxxxxxx'
alice = Aliceblue(user_id=uid,api_key=key)
print(alice.get_session_id()) # Get Session ID

print("datetime.datetime.now()")
print(datetime.datetime.now())
   
now = datetime.datetime.now()
dt915am = datetime.datetime(2023, 1, 6, 9, 15, 3)
dt330pm = datetime.datetime(2023, 1, 6, 15, 30, 00)

orderplacetime = int(9) * 60 + int(15)
timenow = (datetime.datetime.now().hour * 60 + datetime.datetime.now().minute)
print("Waiting for 9.15 AM , CURRENT TIME:{}".format(datetime.datetime.now()))

while timenow < orderplacetime:
    time.sleep(2)
    timenow = (datetime.datetime.now().hour * 60 + datetime.datetime.now().minute)
print("Ready for trading, CURRENT TIME:{}".format(datetime.datetime.now()))

# while True:
#       if(now > dt915am and now < dt330pm):
        #Initialization
sym = 'BANKNIFTY23FEBFUT'
exc = 'NFO'
exp_date="2023-02-23"
option_exp = '2023-02-23'
qty = 25
th_toll = 10
# buy_above = 43140
# sell_below = 43100

# Predefined Functions
def open_or_ltp(give = 'ltp'):
    sym_info = alice.get_scrip_info(alice.get_instrument_for_fno(exch=exc, symbol= sym, expiry_date=exp_date, is_fut=True, strike=None, is_CE=False))
    if give == 'open':
        if 'openPrice' in sym_info:
            return float(sym_info['openPrice'])
        else:
            return 0
    else:
        if 'Ltp' in sym_info:
            return float(sym_info['Ltp'])
        else:
            return 0
           
def round_up(n, decimals=0):
        multiplier = 10 ** decimals
        return np.ceil(n * multiplier) / multiplier
#-------------------------------------------------------------------------------------------------
# While commenting out this section also comment out the custom_order Section and vise versa
#-------------------------------------------------------------------------------------------------
def custom_order(i,q,b_or_s = "B"):
    pprint(alice.place_order(transaction_type = TransactionType.Sell if b_or_s == 'S' else TransactionType.Buy,
                     instrument = i,
                     quantity = q,
                     order_type = OrderType.Market,
                     product_type = ProductType.Intraday,
                     price = 0.0,
                     trigger_price = None,
                     stop_loss = None,
                     square_off = None,
                     trailing_sl = None,
                     is_amo = False,
                     order_tag='order1'))
#-------------------------------------------------------------------------------------------------

# LOGIC
bull_flag = False
bear_flag = False

day_open = open_or_ltp('open')
#day_open = 42868

if day_open > 0:
    ATMStrike = round(float(day_open)/100)*100
    OTM_CE200 = ATMStrike + 200
    OTM_PE200 = ATMStrike - 200
    V1 = math.sqrt(day_open) + 0.035
    V2 = math.pow(V1,2) # resquaring
    V3 = math.sqrt(day_open) + 0.3325 #For T2 0.3325 / For T1 0.165
    V4 = math.pow(V3,2)
    buy_above = round_up(V2,1)
    bull_tg1 = round_up(V4,1)
    V15 = math.sqrt(day_open) - 0.035
    V16 = math.pow(V15,2)
    V17 = math.sqrt(day_open) - 0.3325 #For T2 0.3325 / For T1 0.165
    V18 = math.pow(V17,2)
    sell_below = round_up(V16,1)
    bear_tg1 = round_up(V18,1)
    
    bull_sl = sell_below
    bear_sl = buy_above
    
    #ce_ltp = alice.get_scrip_info(alice.get_instrument_for_fno(exch=exc, symbol= "BANKNIFTY", expiry_date=option_exp, is_fut=False, strike=ATMStrike, is_CE=True))
    #pe_ltp = alice.get_scrip_info(alice.get_instrument_for_fno(exch=exc, symbol= "BANKNIFTY", expiry_date=option_exp, is_fut=False, strike=ATMStrike, is_CE=False))
    
    def CE_or_ltp(give = 'ltp'):
        CE_info = alice.get_scrip_info(alice.get_instrument_for_fno(exch=exc, symbol= "BANKNIFTY", expiry_date=option_exp, is_fut=False, strike=ATMStrike, is_CE=True))
        if give == 'open':
            if 'openPrice' in CE_info:
                return float(CE_info['openPrice'])
            else:
                return 0
        else:
            if 'Ltp' in CE_info:
                return float(CE_info['Ltp'])
            else:
                return 0
    def PE_or_ltp(give = 'ltp'):
        PE_info = alice.get_scrip_info(alice.get_instrument_for_fno(exch=exc, symbol= "BANKNIFTY", expiry_date=option_exp, is_fut=False, strike=ATMStrike, is_CE=False))
        if give == 'open':
            if 'openPrice' in PE_info:
                return float(PE_info['openPrice'])
            else:
                return 0
        else:
            if 'Ltp' in PE_info:
                return float(PE_info['Ltp'])
            else:
                return 0 

    ltp_ce = CE_or_ltp('ltp')
    ltp_pe = PE_or_ltp('ltp')
    #print('ltp_ce==>',ltp_ce)
    #print('ltp_pe==>',ltp_pe)



    while True:
        ltp = open_or_ltp()
        ltp_ce = CE_or_ltp('ltp')
        ltp_pe = PE_or_ltp('ltp')

        if ltp > 0:
            print(f"LTP: {ltp} BA : {buy_above} SB: {sell_below} with {th_toll} point tollorance.")
            print(f"LTP: {ltp} Bull TG1 : {bull_tg1} Bull SL: {bull_sl}")
            print(f"LTP: {ltp} Bear TG1 : {bear_tg1} Bear SL: {bear_sl}")
            bull_inst = alice.get_instrument_for_fno(exch=exc, symbol= "BANKNIFTY", expiry_date=option_exp, is_fut=False, strike=ATMStrike, is_CE=True)
            bear_inst = alice.get_instrument_for_fno(exch=exc, symbol= "BANKNIFTY", expiry_date=option_exp, is_fut=False, strike=ATMStrike, is_CE=False)
            # ENTRY
            if ltp >= buy_above and ltp <= buy_above +th_toll and bull_flag is False:#+th_toll and bull_flag is False:
                print('Push a BUY CE order for ATMStrike', ATMStrike,'CE - Last Traded Price==>',ltp_ce, (datetime.datetime.now()))
                print('ltp_ce==>',ltp_ce)
                ce = pd.DataFrame({'LTP_CE': [ltp_ce]})
                ce.to_csv('BuyTradeCE.csv', mode='a')
                custom_order(bull_inst,qty)
                bull_flag = True
            elif ltp <= sell_below and ltp >= sell_below -th_toll and bear_flag is False:#-th_toll and bear_flag is False:
            # elif ltp <= sell_below and bear_flag is False:
                print('Push a BUY PE order for ATMStrike', ATMStrike,'PE - Last Traded Price==>',ltp_pe, (datetime.datetime.now()))
                print('ltp_pe==>',ltp_pe)
                pe = pd.DataFrame({'LTP_PE': [ltp_pe]})
                pe.to_csv('BuyTradePE.csv', mode='a')
                custom_order(bear_inst,qty)
                bear_flag = True
            else:
                print("No Condition Match or already in an open postion.",(datetime.datetime.now()))
                print('ATMStrike -',ATMStrike,'CE - Last Traded Price==>',ltp_ce)
                print('ATMStrike -',ATMStrike,'PE - Last Traded Price==>',ltp_pe)
            
            # EXIT
            if bull_flag:
                if ltp >= bull_tg1 or ltp <= bull_sl:
                    print("ATM - CE Squared OFF." ,ATMStrike,'CE - Last Traded Price==>',ltp_ce,(datetime.datetime.now()))
                    custom_order(bull_inst,qty, b_or_s="S")
                    print('ltp_ce==>',ltp_ce)
                    ce = pd.DataFrame({'LTP_CE': [ltp_ce]})
                    ce.to_csv('BuyTradeCE.csv', mode='a')
                    bull_flag = False
            else:
                print("Waiting for a BULL postion.",(datetime.datetime.now()))
            
            if bear_flag:
                if ltp <= bear_tg1 or ltp >= bear_sl:
                    print("ATM PE Squared OFF.",ATMStrike,'PE - Last Traded Price==>',ltp_pe,(datetime.datetime.now()))
                    custom_order(bear_inst,qty, b_or_s="S")
                    print('ltp_pe==>',ltp_pe)
                    pe = pd.DataFrame({'LTP_PE': [ltp_pe]})
                    pe.to_csv('BuyTradePE.csv', mode='a')
                    bear_flag = False
            else:
                print("Waiting for a BEAR postion.", (datetime.datetime.now()))
        else:
            print("LTP Not Found")
        
        time.sleep(0.6)
else:
    print("Open Price Not Found")


      # else:

      #    if (now > dt330pm):
      #       print("not between 9:15 and 3:30. so exiting.")
      #       break







