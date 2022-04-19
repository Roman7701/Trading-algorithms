Only one Trading Stratergy as of yet.

It's is the VWAP trading stratergy .

VWAP stands for Volumated weighted average price.It is a popular indicator among day traders as well institutions.It is calculated via:

		TypicalPrice=(high+low+close)/3

		vwap=Σ(TypicalPrice*volume)/Σ volume

So basically the goal is to make an entry based upon the position of candles with respect to the vwap values. If the candles move above the VWAP then it indicates as a bullish sentiment and therefore a reason to enter a long position.If the candles move below the VWAP ,then it indicates a brearish momentum and therfore a reason to enter a short position. 


I am currently using pandas_ta to manage data and leverage existing methods to make my work easier . The problem is that there seems to be some sort of bug in the vwap funciton of the library ,so I head to manually write the code.

NOTE:WORKS ONLY ON 15m TIMEFRAMES.

Although this stratergy triggers a lot of false positives , it can actually be compensated by adjusting leverages and taking profits at targetted levels.This way you could roughly execute 100-120 trades a month and probably snatch off a PNL of 170%.

Will develop this algorithm further and try to write code to connect to Binance api and execute trades.


I have explained the trading stratergy pretty cleary . If you still didnt understand anything , I can't help you in any way .If you are smart enough ,you could use this algorithm and connect it to Binance api and make some money .

You can use this code to test out the max possible profits you can achieve in a day(Not losses).


NOTE:You have to adjust the number candles while fetching data in the code because vwap values are calculated based on the start of the day.


WILL DEVELOP MORE STRATERGIES AND I AM JUST A BEGINER SO NO HATE ON LMAOO.
Until Next time!!
