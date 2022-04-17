import pandas_ta as ta
import pandas as pd
import ccxt
from pandas_ta.utils import get_offset, is_datetime_ordered, verify_series



def MyVwap(df):

	

	CumTPxVol=0
	CumVol=0

	ResVWAP={}
	ResVWAP["time"]=[]
	ResVWAP["TP"]=[]

	for cand in range(df.shape[0]):
		print(df.index[cand].isoformat())
		CumTPxVol+=((df['high'][cand]+df['low'][cand]+df['close'][cand])/3)*df['volume'][cand]
		CumVol+=df['volume'][cand]

		volumated_average_price=CumTPxVol/CumVol

		ResVWAP["time"].append(df.index[cand])
		ResVWAP["TP"].append(volumated_average_price)

			
	return pd.DataFrame(ResVWAP)





#Fetching and storing values
exchange = ccxt.binance()
bars = exchange.fetch_ohlcv('BTC/USDT', timeframe='15m', limit=65)
df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
df['time'] = pd.to_datetime(df['time'], unit='ms')
df.set_index("time",inplace=True)

vwap=MyVwap(df)
# print(vwap)



#returning my own function of calculating vwap values





# #dry run 
# position=False
# hit=0
# miss=0
# percentage_gain_frequency=[]
# Long_or_short=False
# balance_in_dollars=300
# spot=0
# profit=0

# for i in range(20):
# 	percentage_gain_frequency.append(50)


# entry=None
# for i in range(50):
# 	#checking for an entry in long position
# 	if df['open']>vwap[i] and !Long_or_short:

# 		if entry!=None:



# 		entry=df['open']
# 		Long_or_short=True

# 	#checking for an entry in short position
# 	if df['open']<vwap[i] and Long_or_short:


# 		if entry !=None:


# 		entry=df['open']
# 		Long_or_short=False






