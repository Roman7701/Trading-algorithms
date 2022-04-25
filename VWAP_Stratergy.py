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
bars = exchange.fetch_ohlcv('BTC/USDT', timeframe='15m', limit=75)
df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
df['time'] = pd.to_datetime(df['time'], unit='ms')
df.set_index("time",inplace=True)





vwap=MyVwap(df)
#returning my own function of calculating vwap values

# print(df.ta.vwap())





#Testing out profits(not losses) on btc 15m timeframe

profits=[]
losses=[]

IsAboveVWAP=False
IsBelowVWAP=False

entry=0

minVal=0
maxVal=0



#Trade variables 

balance=130
position=130
tp=[0,0,0,0]
ProfitsMarks=[4,8,14,20]
sl=0
PNL=0
leverage=20
qrtr=0




tpStatus=[False,False,False,False]
TradeIsOpen=False



for value in range(vwap.shape[0]):


	if(df["open"][value]>vwap["VWAP"][value] and IsAboveVWAP):
		if(TradeIsOpen==False):
			continue


		minVal=min(df["low"][value],minVal)
		maxVal=max(df["high"][value],minVal)

		if(minVal<=sl):
			balance+=position/2
			position=0
			tp=[0,0,0,0]
			tpStatus=[False,False,False,False]
			TradeIsOpen=False
			continue

		else:
			for i in range(4):

				if(maxVal>=tp[i] and tpStatus[i]==False):
					position-=qrtr
					balance+=qrtr*(100+ProfitsMarks[i])
					tpStatus[i]=True

			if(tpStatus[3]):
				TradeIsOpen=False

			continue




	if(df["open"][value]>vwap["VWAP"][value] and IsAboveVWAP==False):

		

		if(TradeIsOpen):
			position=position*(100-((df["open"][value]-entry)/100))
			balance=position
			tp=[0,0,0,0]
			tpStatus=[False,False,False,False]	


		entry=df["open"][value]

		IsAboveVWAP=True
		IsBelowVWAP=False
		TradeIsOpen=True

		tp[0]=entry*(100+(4/leverage))
		tp[1]=entry*(100+(8/leverage))
		tp[2]=entry*(100+(14/leverage))
		tp[3]=entry*(101)
		tpStatus=[False,False,False,False]
		sl=entry*(100-(50/leverage))


		position=balance
		balance=0
		qrtr=position/4
		minVal=df["low"][value]
		maxVal=df["high"][value]

		continue




	if(df["open"][value]<vwap["VWAP"][value] and IsBelowVWAP):

		if(TradeIsOpen==False):
			continue

		minVal=min(df["low"][value],minVal)
		maxVal=min(df["high"][value],minVal)


		if(maxVal>=sl):
			balance+=position/2
			position=0
			tp=[0,0,0,0]
			tpStatus=[False,False,False,False]
			TradeIsOpen=False
			continue

		else:

			for i in range(4):
				if(minVal<=tp[i] and tpStatus[i]==False):
					position-=qrtr
					balance+=qrtr*(100+ProfitsMarks[i])
					tpStatus[i]=True

			if(tpStatus[3]):
				TradeIsOpen=False

				continue


		

	if(df["open"][value]<vwap["VWAP"][value] and IsBelowVWAP==False):



		if(TradeIsOpen):
			position=position*(100-((entry-df["open"][value])/100))
			balance=position
			tp=[0,0,0,0]
			tpStatus=[False,False,False,False]	



		entry=df["open"][value]
		IsAboveVWAP=False
		IsBelowVWAP=True
		TradeIsOpen=True


		tp[0]=entry*(100-(4/leverage))
		tp[1]=entry*(100-(8/leverage))
		tp[2]=entry*(100-(14/leverage))
		tp[3]=entry*(99)
		sl=entry*(100+(50/leverage))


		position=balance
		balance=0
		qrtr=position/4

		minVal=df["low"][value]
		maxVal=df["high"][value]


		continue





print(balance)














