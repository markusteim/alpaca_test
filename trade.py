import pandas as pd
import numpy as np
import scipy as sc
from alpaca_trade_api.stream import Stream, URL

async def trade_callback(t):
    print('trade', t)


async def quote_callback(q):
    print('quote', q)


# Initiate Class Instance
stream = Stream('PK4FYPZ9LRV2Y9ESSDKY',
                '2lQ7T1ByQCDH4UeAEAe9021rupqlQMbTUMXW077Y',
                base_url=URL('https://paper-api.alpaca.markets'),
                data_feed='iex')  # <- replace to SIP if you have PRO subscription

# subscribing to event
stream.subscribe_trades(trade_callback, 'AAPL')
stream.subscribe_quotes(quote_callback, 'IBM')

stream.run()