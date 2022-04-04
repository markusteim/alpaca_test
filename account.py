import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import URL



api = tradeapi.REST('PK4FYPZ9LRV2Y9ESSDKY','2lQ7T1ByQCDH4UeAEAe9021rupqlQMbTUMXW077Y',base_url=URL('https://paper-api.alpaca.markets'))

account = api.get_account()

if account.status == "ACTIVE":
    #get as many stocks as possible and select the one that has the largest drop through out the day
    #and buy it for a day
    api.submit_order(
    symbol='SPY',
    side='buy',
    type='market',
    qty='15',
    time_in_force='day',
    order_class='bracket',
    take_profit=dict(
        limit_price='500.0',
    ),
    stop_loss=dict(
        stop_price='450.',
        limit_price='450.0',
    )
)


