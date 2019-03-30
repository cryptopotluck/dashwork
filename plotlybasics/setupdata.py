from alpha_vantage.timeseries import TimeSeries
from alpha_vantage import foreignexchange
from alpha_vantage.foreignexchange import ForeignExchange
from pandas import DataFrame as df
#ts = TimeSeries(key='G8L62BYFX5JJH9QX', retries=10, output_format='pandas', indexing_type='date')
# Get json object with the intraday data and another with  the call's metadata


#foreign = ForeignExchange(function='CURRENCY_EXCHANGE_RATE', from_currency='BTC', to_currency='USD', key='G8L62BYFX5JJH9QX' )

foreign2 = ForeignExchange(key='G8L62BYFX5JJH9QX', retries=10, output_format='pandas')

foreign_data, meta_data = foreign2.get_currency_exchange_intraday(from_symbol='CAN', to_symbol='USD')
#data, meta_data = ts.get_intraday(symbol='DJI',interval='1min', outputsize='full')
print(foreign_data[0][99:])