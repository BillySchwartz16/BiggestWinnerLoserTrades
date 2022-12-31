import yahoo_fin.stock_info as si


gainers = si.get_day_losers()


print(gainers)