from pya3 import *
from collections import namedtuple
import datetime as datetime
import pandas as pd
import os
import json
# import time
import schedule
from datetime import datetime, timedelta
import datetime
import time
import math
import numpy as np
import pdb
import telegram
from telegram.ext import Updater, CommandHandler
from io import StringIO
updater = Updater(token='5677013393:AAHkHd0QwFX5MyglPzCsnLJiQ3zJ9GezF9s', use_context=True)

# Define a function to send the output to the group
def send_output(output):
	# Send the output to the group
	updater.bot.send_message(chat_id='-1001744638066', text=output)
	updater.bot.send_message(chat_id='-1001842144538', text=output)
	#updater.bot.send_message(chat_id='1842144538', text=output)
	#updater.bot.send_message(chat_id='1386767482', text=output)

# Redirect the output of the print command to a string
with StringIO() as output:

# def alert_bot(bot_message):
#     try:
#         msg = 'https://api.telegram.org/bot' + {{5677013393:AAHkHd0QwFX5MyglPzCsnLJiQ3zJ9GezF9s}} + '/sendMessage?chat_id=' + {{-1001744638066}} + \
#                     '&parse_mode=HTML&text=' + html.escape(bot_message)
		
#         response = requests.get(msg)

#         return response.json()
#     except Exception as e:
#         s_logger.exception(f'Error in alerting {e}')
  
# #Replace {{5677013393:AAHkHd0QwFX5MyglPzCsnLJiQ3zJ9GezF9s}} and {{-1001744638066}} with ur values


	user_id = '488059'
	api_key = '7iHGrc5U468s65OV6Sa27xyHmIE6alX2dypSEZhbF2IXsHBz3Z4zdbIrss7bWt72QZf6bnpYfWac8BJxMTAfgKs9zqRunB9HyT9UoaeKsIj2ZOe2nMVZU6kxQEMDVvKN'

	alice = Aliceblue(user_id=user_id, api_key=api_key)

	print(alice.get_session_id())

	def round_up(n, decimals=0):
		multiplier = 10 ** decimals
		return np.ceil(n * multiplier) / multiplier

	##stock_data_list
	# watchlist = ['HDFCBANK']#, 'AXISBANK', 'ICICIBANK']

	# exch = 'NSE'
	##fut_data_list
	watchlist1 = ['BANKNIFTY']#, 'NIFTY']
	exchng = 'NFO'
	traded_stocks = []
	print('traded_stocks ===> ',traded_stocks)
	Sell_fut_index = []
	print('Sell_fut_index ===> ',Sell_fut_index)

	# upper_symbol_instrument = alice.get_instrument_for_fno(exch="NFO",symbol= fut, expiry_date="2022-12-29", is_fut=True, strike=None, is_CE=False)
	first_entry = False
	while True:

		# for stock in watchlist:

			for fut in watchlist1:

				# Ltp_Stock1 = alice.get_scrip_info(alice.get_instrument_by_symbol(exch, stock))['Ltp']
				# Ltp_Stock = float(Ltp_Stock1)
				# print(alice.get_scrip_info(alice.get_instrument_by_symbol('NFO', 'BANKNIFTY'))['Ltp'])
				Ltp_Fut1 = alice.get_scrip_info(alice.get_instrument_for_fno(exch=exchng, symbol= fut, expiry_date="2023-01-25", is_fut=True, strike=None, is_CE=False))['Ltp']
				Ltp_Fut = float(Ltp_Fut1) #tick price
				#Ltp_Fut1.to_json("03-jan-LTPdata.json", mode='a')
				if first_entry == False:
					first_entry = True 
					Ltp_Fut_old = Ltp_Fut 

				#print("Ltp of ", stock, Ltp_Stock)
				print("Current Time", (datetime.datetime.now()))
				#print(datetime.datetime.now())
				print("LTP of ", fut, Ltp_Fut1,"==|== OLD LTP", Ltp_Fut_old )#, file=output)	# Enter time
					



				##pulling_fut_Buy_condition_from_here!!!
				DayOpen = float(alice.get_scrip_info(alice.get_instrument_for_fno(exch=exchng, symbol= fut, expiry_date="2023-01-25", is_fut=True, strike=None, is_CE=False))['openPrice'])#df["open"].iloc[0]
				#print(DayOpen)
				# CEOTMStrike = round(float(DayOpen)/100)*100+200
				# PEOTMStrike = round(float(DayOpen)/100)*100-200
				# print(CEOTMStrike)
				# print(PEOTMStrike)
				ATMStrike = round(float(DayOpen)/100)*100
				 #ATM = round(float(LTP)/100) * 100
				#print('ATMStrike =', file=output)
				# pdb.set_trace()
				expiry_date = "2023-01-05"# Option weekly expiry Dates 2023-01-05 or 2023-01-12 or 2023-01-19 or 2023-01-25
				qty_fut = 25
				qty_stock = 500
				# traded_stocks = []

				CDO = DayOpen
				V1 = math.sqrt(CDO) + 0.035
				V2 = math.pow(V1,2) # resquaring
				Buyabove = round_up(V2,1)
				print('Buy Only Above in index= ',Buyabove, 'in', fut)

				V3 = math.sqrt(CDO) + 0.165
				V4 = math.pow(V3,2)
				Target1 = round_up(V4,1)
				BT1Earning = round_up(Target1 - Buyabove)
				# print('Buy Target 1 = ',Target1, 'If Target Hit....Earning in Points = ', BT1Earning )


				V5 = math.sqrt(CDO) + 0.3325
				V6 = math.pow(V5,2)
				Target2 = round_up(V6,1)
				BT2Earning = round_up(Target2 - Buyabove)
				# print('Buy Target 2 = ',Target2, 'If Target Hit....Earning in Points = ', BT2Earning)

				V7 = math.sqrt(CDO) + 0.4825
				V8 = math.pow(V7,2)
				Target3 = round_up(V8,1)
				BT3Earning = round_up(Target3 - Buyabove)
				# print('Buy Target 3 = ',Target3, 'If Target Hit....Earning in Points = ', BT3Earning)

				V9 = math.sqrt(CDO) + 0.6125
				V10 = math.pow(V9,2)
				Target4 = round_up(V10,1)
				BT4Earning = round_up(Target4 - Buyabove)
				# print('Buy Target 4 = ',Target4, 'If Target Hit....Earning in Points = ', BT4Earning)

				V11 = math.sqrt(CDO) + 0.8125
				V12 = math.pow(V11,2)
				Target5 = round_up(V12,1)
				BT5Earning = round_up(Target5 - Buyabove)
				# print('Buy Target 5 = ',Target5, 'If Target Hit....Earning in Points = ', BT5Earning)

				V13 = math.sqrt(CDO) - 0.035
				V14 = math.pow(V13,2)
				BuyStop = round_up(V14,1)
				BuyStopLoss = round_up(Buyabove - BuyStop )
				# print("Buy Stop Loss = ",BuyStop, 'If Stop Loss Hit....Loss in Points = ', BuyStopLoss)
				 
				#pulling_fut_sell_cond_from_here!!!

				V15 = math.sqrt(CDO) - 0.035
				V16 = math.pow(V15,2)
				Sellbelow = round_up(V16,1)
				print('Sell Only Below in index = ',Sellbelow, 'in', fut)

				V17 = math.sqrt(CDO) - 0.165
				V18 = math.pow(V17,2)
				DTarget1 = round_up(V18,1)
				ST1Earning = round_up(Sellbelow - DTarget1)
				# print('Sell Target 1 = ',DTarget1, 'If Target Hit....Earning in Points = ', ST1Earning)

				V19 = math.sqrt(CDO) - 0.3325
				V20 = math.pow(V19,2)
				DTarget2 = round_up(V20,1)
				ST2Earning = round_up(Sellbelow - DTarget2)
				# print('Sell Target 2 = ',DTarget2, 'If Target Hit....Earning in Points = ', ST2Earning)

				V21 = math.sqrt(CDO) - 0.4825
				V22 = math.pow(V21,2)
				DTarget3 = round_up(V22,1)
				ST3Earning = round_up(Sellbelow - DTarget3)
				# print('Sell Target 3 = ',DTarget3, 'If Target Hit....Earning in Points = ', ST3Earning)

				V23 = math.sqrt(CDO) - 0.6125
				V24 = math.pow(V23,2)
				DTarget4 = round_up(V24,1)
				ST4Earning = round_up(Sellbelow - DTarget4)
				# print('Sell Target 4 = ',DTarget4, 'If Target Hit....Earning in Points = ', ST4Earning)

				V25 = math.sqrt(CDO) - 0.8125
				V26 = math.pow(V25,2)
				DTarget5 = round_up(V26,1)
				ST5Earning = round_up(Sellbelow - DTarget5)
				# print('Sell Target 5 = ',DTarget5, 'If Target Hit....Earning in Points = ', ST5Earning)

				V27 = math.sqrt(CDO) + 0.035
				V28 = math.pow(V27,2)
				SellStop = round_up(V28,1)
				SellStopLoss = round_up(SellStop - Sellbelow )
				# print("Sell Stop Loss = ",SellStop, 'If Stop Loss Hit....Loss in Points = ', SellStopLoss)

				#pulling_stock_buy_cond_from_here!!!

				# stock_open = float(alice.get_scrip_info(alice.get_instrument_by_symbol(exch, stock))['openPrice'])
				# # print(stock_open)

				# CDO_STK = stock_open


				# V1 = math.sqrt(CDO_STK) + 0.035
				# V2 = math.pow(V1,2)
				# Buyabove_stk = round_up(V2,1)
				# print('Buy Only Above in stocks  = ',Buyabove_stk, 'in', stock)

				# V3 = math.sqrt(CDO_STK) + 0.165
				# V4 = math.pow(V3,2)
				# Target1_stk = round_up(V4,1)
				# BT1Earning = round_up(Target1_stk - Buyabove_stk)
				# # print('Buy Target 1 = ',Target1_stk, 'If Target Hit....Earning in Points = ', BT1Earning )


				# V5 = math.sqrt(CDO_STK) + 0.3325
				# V6 = math.pow(V5,2)
				# Target2_stk = round_up(V6,1)
				# BT2Earning = round_up(Target2_stk - Buyabove_stk)
				# # print('Buy Target 2 = ',Target2_stk, 'If Target Hit....Earning in Points = ', BT2Earning)

				# V7 = math.sqrt(CDO_STK) + 0.4825
				# V8 = math.pow(V7,2)
				# Target3_stk = round_up(V8,1)
				# BT3Earning = round_up(Target3_stk - Buyabove_stk)
				# # print('Buy Target 3 = ',Target3_stk, 'If Target Hit....Earning in Points = ', BT3Earning)

				# V9 = math.sqrt(CDO_STK) + 0.6125
				# V10 = math.pow(V9,2)
				# Target4_stk = round_up(V10,1)
				# BT4Earning = round_up(Target4_stk - Buyabove_stk)
				# # print('Buy Target 4 = ',Target4_stk, 'If Target Hit....Earning in Points = ', BT4Earning)

				# V11 = math.sqrt(CDO_STK) + 0.8125
				# V12 = math.pow(V11,2)
				# Target5_stk = round_up(V12,1)
				# BT5Earning = round_up(Target5_stk - Buyabove_stk)
				# # print('Buy Target 5 = ',Target5_stk, 'If Target Hit....Earning in Points = ', BT5Earning)

				# V13 = math.sqrt(CDO_STK) - 0.035
				# V14 = math.pow(V13,2)
				# BuyStop_stk = round_up(V14,1)
				# BuyStopLoss = round_up(Buyabove_stk - BuyStop_stk )
				# # print("Buy Stop Loss = ",BuyStop_stk, 'If Stop Loss Hit....Loss in Points = ', BuyStopLoss)


				# V15 = math.sqrt(CDO_STK) - 0.035
				# V16 = math.pow(V15,2)
				# Sellbelow_stk = round_up(V16,1)
				# print('Sell Only Below in stocks = ',Sellbelow_stk, 'in', stock)

				# V17 = math.sqrt(CDO_STK) - 0.165
				# V18 = math.pow(V17,2)
				# STK_Target1 = round_up(V18,1)
				# ST1Earning = round_up(Sellbelow_stk - STK_Target1)
				# # print('Sell Target 1 = ',STK_Target1, 'If Target Hit....Earning in Points = ', ST1Earning)

				# V19 = math.sqrt(CDO_STK) - 0.3325
				# V20 = math.pow(V19,2)
				# STK_Target2 = round_up(V20,1)
				# ST2Earning = round_up(Sellbelow_stk - STK_Target2)
				# # print('Sell Target 2 = ',STK_Target2, 'If Target Hit....Earning in Points = ', ST2Earning)

				# V21 = math.sqrt(CDO_STK) - 0.4825
				# V22 = math.pow(V21,2)
				# STK_Target3 = round_up(V22,1)
				# ST3Earning = round_up(Sellbelow_stk - STK_Target3)
				# # print('Sell Target 3 = ',STK_Target3, 'If Target Hit....Earning in Points = ', ST3Earning)

				# V23 = math.sqrt(CDO_STK) - 0.6125
				# V24 = math.pow(V23,2)
				# STK_Target4 = round_up(V24,1)
				# ST4Earning = round_up(Sellbelow_stk - STK_Target4)
				# # print('Sell Target 4 = ',STK_Target4, 'If Target Hit....Earning in Points = ', ST4Earning)

				# V25 = math.sqrt(CDO_STK) - 0.8125
				# V26 = math.pow(V25,2)
				# STK_Target5 = round_up(V26,1)
				# ST5Earning = round_up(Sellbelow_stk - STK_Target5)
				# # print('Sell Target 5 = ',STK_Target5, 'If Target Hit....Earning in Points = ', ST5Earning)

				# V27 = math.sqrt(CDO_STK) + 0.035
				# V28 = math.pow(V27,2)
				# SellStop_stk = round_up(V28,1)
				# SellStopLoss = round_up(SellStop_stk - Sellbelow_stk )
				# print("Sell Stop Loss = ",SellStop_stk, 'If Stop Loss Hit....Loss in Points = ', SellStopLoss)

				##fut_buy_sell_condition_start_from_here!!!
				traded_stocks = []
				Sell_fut_index = []
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
				#ATM CE BUY or SELL or STOP LOSS HIT condition starts here!!!

				if (Buyabove <= Ltp_Fut ) and (Buyabove > Ltp_Fut_old ) and (fut not in traded_stocks): # Change to Buyabove

					upper_symbol_instrument = alice.get_instrument_for_fno(exch=exchng, symbol= fut, expiry_date=expiry_date, is_fut=False, strike=ATMStrike, is_CE=True)

					order = alice.place_order(transaction_type = TransactionType.Buy,
												instrument = alice.get_instrument_by_symbol(exchng, upper_symbol_instrument.name),
												quantity =qty_fut,
												order_type = OrderType.Market,
												product_type = ProductType.Intraday,
												price = 0.0,
												trigger_price = None,
												stop_loss = None,
												square_off = None,
												trailing_sl = None,
												is_amo = False,
												order_tag='order1')
					print(order)
					traded_stocks.append(fut)
					print(traded_stocks)
					print("Buy order placed in ATM CE:", fut, ATMStrike)

				if (Target1 <= Ltp_Fut) and (Target1 > Ltp_Fut_old ) and (fut in traded_stocks):# or (Target2 <= Ltp_Fut) and (fut not in traded_stocks) or (Target3 <= Ltp_Fut) and (fut not in traded_stocks) or (Target4 <= Ltp_Fut) and (fut not in traded_stocks) or (Target5 <= Ltp_Fut) and (fut not in traded_stocks):

					upper_symbol_instrument = alice.get_instrument_for_fno(exch=exchng, symbol=fut, expiry_date=expiry_date, is_fut=False, strike=ATMStrike, is_CE=True)

					order = alice.place_order(transaction_type = TransactionType.Sell,
												instrument = alice.get_instrument_by_symbol(exchng, upper_symbol_instrument.name),
												quantity =qty_fut,
												order_type = OrderType.Market,
												product_type = ProductType.Intraday,
												price = 0.0,
												trigger_price = None,
												stop_loss = None,
												square_off = None,
												trailing_sl = None,
												is_amo = False,
												order_tag='order1')
					print(order)					
					traded_stocks.append(fut)
					print(traded_stocks)
					traded_stocks = []
					print("Target hit in ATM CE Buy order:", fut, ATMStrike)

				if (BuyStop >= Ltp_Fut) and (BuyStop < Ltp_Fut_old )and (fut in traded_stocks):

					upper_symbol_instrument = alice.get_instrument_for_fno(exch=exchng, symbol= fut, expiry_date=expiry_date, is_fut=False, strike=ATMStrike, is_CE=True)

					order = alice.place_order(transaction_type = TransactionType.Sell,
												instrument = alice.get_instrument_by_symbol(exchng, upper_symbol_instrument.name),
												quantity =qty_fut,
												order_type = OrderType.Market,
												product_type = ProductType.Intraday,
												price = 0.0,
												trigger_price = None,
												stop_loss = None,
												square_off = None,
												trailing_sl = None,
												is_amo = False,
												order_tag='order1')
					print(order)					
					traded_stocks.append(fut)
					print(traded_stocks)
					traded_stocks = []
					print("Stop loss hit in ATM CE Buy order:", fut, ATMStrike)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
				#ATM PE BUY or SELL or STOP LOSS HIT condition starts here!!!

				if (Sellbelow >= Ltp_Fut) and (Sellbelow < Ltp_Fut_old ) and (fut not in Sell_fut_index):

					lower_symbol_instrument = alice.get_instrument_for_fno(exch=exchng, symbol= fut, expiry_date=expiry_date, is_fut=False, strike=ATMStrike, is_CE=False)

					order = alice.place_order(transaction_type = TransactionType.Buy,
												instrument = alice.get_instrument_by_symbol(exchng, lower_symbol_instrument.name),
												quantity = qty_fut,
												order_type = OrderType.Market,
												product_type = ProductType.Intraday,
												price = 0.0,
												trigger_price = None,
												stop_loss = None,
												square_off = None,
												trailing_sl = None,
												is_amo = False,
												order_tag='order1')
					print(order)
					Sell_fut_index.append(fut)
					print(Sell_fut_index)
					print("Buy oredr placed in ATM PE :", fut, ATMStrike )

				if (DTarget2 >= Ltp_Fut) and (DTarget2 < Ltp_Fut_old ) and (fut in Sell_fut_index): #or (DTarget2 >= Ltp_Fut) and (fut not in traded_stocks): #or (DTarget3 >= Ltp_Fut) or (DTarget4 >= Ltp_Fut) or (DTarget4 >= Ltp_Fut) and (fut not in traded_stocks):


					lower_symbol_instrument = alice.get_instrument_for_fno(exch=exchng, symbol= fut, expiry_date=expiry_date, is_fut=False, strike=ATMStrike, is_CE=False)
					order = alice.place_order(transaction_type = TransactionType.Sell,
												instrument = alice.get_instrument_by_symbol(exchng, lower_symbol_instrument.name),
												quantity =qty_fut,
												order_type = OrderType.Market,
												product_type = ProductType.Intraday,
												price = 0.0,
												trigger_price = None,
												stop_loss = None,
												square_off = None,
												trailing_sl = None,
												is_amo = False,
												order_tag='order1')
					print(order)
					Sell_fut_index.append(fut)
					print(Sell_fut_index)
					Sell_fut_index = []
					print("Target hit in ATM PE Buy order :", fut, ATMStrike)

				if (SellStop <= Ltp_Fut) and (SellStop > Ltp_Fut_old )  and (fut in Sell_fut_index):

					lower_symbol_instrument = alice.get_instrument_for_fno(exch=exchng, symbol= fut, expiry_date=expiry_date, is_fut=False, strike=ATMStrike, is_CE=False)
					order = alice.place_order(transaction_type = TransactionType.Sell,
												instrument = alice.get_instrument_by_symbol(exchng, lower_symbol_instrument.name),
												quantity =qty_fut,
												order_type = OrderType.Market,
												product_type = ProductType.Intraday,
												price = 0.0,
												trigger_price = None,
												stop_loss = None,
												square_off = None,
												trailing_sl = None,
												is_amo = False,
												order_tag='order1')
					print(order)
					Sell_fut_index.append(fut)
					print(Sell_fut_index)
					Sell_fut_index = []
					print("Stoploss hit in ATM PE Buy order:", fut, ATMStrike)

				# ##stock_buy_sell_condition_start_from_here!!!

				# if (Buyabove_stk <= Ltp_Stock ) and (stock not in traded_stocks):

				# 	order = alice.place_order(transaction_type = TransactionType.Buy,
				# 								instrument = alice.get_instrument_by_symbol(exch, stock),
				# 								quantity =qty_stock,
				# 								order_type = OrderType.Market,
				# 								product_type = ProductType.Intraday,
				# 								price = 0.0,
				# 								trigger_price = None,
				# 								stop_loss = None,
				# 								square_off = None,
				# 								trailing_sl = None,
				# 								is_amo = False,
				# 								order_tag='order1')
				# 	print(order)
				# 	traded_stocks.append(stock)

				# 	print("Buy order placed in stock :", stock)

				# if (Target1_stk <= Ltp_Stock) or (Target2_stk <= Ltp_Stock) or (Target3_stk <= Ltp_Stock) or (Target4_stk <= Ltp_Stock) or (Target5_stk <= Ltp_Stock) and (stock not in traded_stocks):

				# 	order = alice.place_order(transaction_type = TransactionType.Sell,
				# 								instrument = alice.get_instrument_by_symbol(exch, stock),
				# 								quantity =qty_stock,
				# 								order_type = OrderType.Market,
				# 								product_type = ProductType.Intraday,
				# 								price = 0.0,
				# 								trigger_price = None,
				# 								stop_loss = None,
				# 								square_off = None,
				# 								trailing_sl = None,
				# 								is_amo = False,
				# 								order_tag='order1')
				# 	print(order)
				# 	traded_stocks.append(stock)

				# 	print("Target hit in stock:", stock)

				# if (BuyStop_stk >= Ltp_Stock) and (stock not in traded_stocks):

				# 	order = alice.place_order(transaction_type = TransactionType.Sell,
				# 								instrument = alice.get_instrument_by_symbol(exch, stock),
				# 								quantity =qty_stock,
				# 								order_type = OrderType.Market,
				# 								product_type = ProductType.Intraday,
				# 								price = 0.0,
				# 								trigger_price = None,
				# 								stop_loss = None,
				# 								square_off = None,
				# 								trailing_sl = None,
				# 								is_amo = False,
				# 								order_tag='order1')
				# 	print(order)
				# 	traded_stocks.append(stock)
				# 	print("Stoploss hit in buy order in stock:", stock)

				# ##stock_sell_condition_from_here!!!

				# if (Sellbelow_stk >= Ltp_Stock) and (stock not in traded_stocks):

				# 	order = alice.place_order(transaction_type = TransactionType.Sell,
				# 								instrument = alice.get_instrument_by_symbol(exch, stock),
				# 								quantity =qty_stock,
				# 								order_type = OrderType.Market,
				# 								product_type = ProductType.Intraday,
				# 								price = 0.0,
				# 								trigger_price = None,
				# 								stop_loss = None,
				# 								square_off = None,
				# 								trailing_sl = None,
				# 								is_amo = False,
				# 								order_tag='order1')
				# 	print(order)
				# 	traded_stocks.append(stock)

				# 	print("Sell order placed in:", stock)

				# if (STK_Target1 >= Ltp_Stock) or (STK_Target2 >= Ltp_Stock) or (STK_Target3 >= Ltp_Stock) or (STK_Target4 >= Ltp_Stock) or (STK_Target5 >= Ltp_Stock) and (stock not in traded_stocks):

				# 	order = alice.place_order(transaction_type = TransactionType.Sell,
				# 								instrument = alice.get_instrument_by_symbol(exch, stock),
				# 								quantity =qty_stock,
				# 								order_type = OrderType.Market,
				# 								product_type = ProductType.Intraday,
				# 								price = 0.0,
				# 								trigger_price = None,
				# 								stop_loss = None,
				# 								square_off = None,
				# 								trailing_sl = None,
				# 								is_amo = False,
				# 								order_tag='order1')
				# 	print(order)
				# 	traded_stocks.append(stock)

				# 	print("Target hit in sell ordered stock:", stock )

				# if (SellStop_stk <= Ltp_Stock) and (stock not in traded_stocks):

				# 	order = alice.place_order(transaction_type = TransactionType.Sell,
				# 								instrument = alice.get_instrument_by_symbol(exch, stock),
				# 								quantity =qty_stock,
				# 								order_type = OrderType.Market,
				# 								product_type = ProductType.Intraday,
				# 								price = 0.0,
				# 								trigger_price = None,
				# 								stop_loss = None,
				# 								square_off = None,
				# 								trailing_sl = None,
				# 								is_amo = False,
				# 								order_tag='order1')
				# 	print(order)
				# 	traded_stocks.append(stock)
				# 	print("Stoploss order hit in sell stock:", stock)

				Ltp_Fut_old = Ltp_Fut
send_output(output.getvalue())
#Ltp_Fut_old = Ltp_Fut
time.sleep(0.8)



