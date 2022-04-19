import pandas_ta as ta
import pandas as pd
import ccxt
from pandas_ta.utils import get_offset, is_datetime_ordered, verify_series



def MyVwap(df):

	

	CumTPxVol=0
	CumVol=0

	ResVWAP={}
	ResVWAP["time"]=[]
	ResVWAP["VWAP"]=[]

	for cand in range(df.shape[0]):

		CumTPxVol+=((df['high'][cand]+df['low'][cand]+df['close'][cand])/3)*df['volume'][cand]
		CumVol+=df['volume'][cand]

		volumated_average_price=CumTPxVol/CumVol

		ResVWAP["time"].append(df.index[cand])
		ResVWAP["VWAP"].append(volumated_average_price)

			
	return pd.DataFrame(ResVWAP)





#Fetching and storing values
exchange = ccxt.binance()
bars = exchange.fetch_ohlcv('BTC/USDT', timeframe='15m', limit=161)
df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
df['time'] = pd.to_datetime(df['time'], unit='ms')
df.set_index("time",inplace=True)





vwap=MyVwap(df)
#returning my own function of calculating vwap values







#Testing out profits(not losses) on btc 15m timeframe
balance=100
profits=[]
losses=[]

IsAboveVWAP=False
IsBelowVWAP=False

entry=0
minmaxVal=0



for value in range(vwap.shape[0]):


	if(df["open"][value]>vwap["VWAP"][value] and IsAboveVWAP):
		minmaxVal=max(minmaxVal,df["high"][value])
		continue
	if(df["open"][value]>vwap["VWAP"][value] and IsAboveVWAP==False):

		if(IsBelowVWAP==True):
			if(minmaxVal>entry):
				losses.append(((minmaxVal-entry)/entry)*100)

			else:
				profits.append(((entry-minmaxVal)/entry)*100)


		IsAboveVWAP=True
		IsBelowVWAP=False
		entry=df["open"][value]
		minmaxVal=df["high"][value]
		continue




	if(df["open"][value]<vwap["VWAP"][value] and IsBelowVWAP):
		minmaxVal=min(minmaxVal,df["low"][value])
		continue

	if(df["open"][value]<vwap["VWAP"][value] and IsBelowVWAP==False):

		if(IsAboveVWAP==True):
			if(minmaxVal>entry):
				profits.append(((minmaxVal-entry)/entry)*100)

			else:
				losses.append(((entry-minmaxVal)/entry)*100)




		IsBelowVWAP=True
		IsAboveVWAP=False
		entry=df["open"][value]
		minmaxVal=df["low"][value]
		continue

print(profits,losses)














