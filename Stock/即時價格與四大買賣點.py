import twstock
def get_price(stockid):
    rt = twstock.realtime.get(stockid)
    if rt['success']:
        return (rt['info']['name'],
        float(rt['realtime']['latest_trade_price']))
    else:
        return(False,False)
def get_best(stockid):
    stock = twstock.Stock(stockid)
    bp = twstock.BestFourPoint(stock).best_four_point()
    if(bp):
        return ('買進' if bp[0] else '賣出',bp[1])
    else:
        return(False,False)
name,price = get_price('2345')
act,why = get_best('2345')
print(name,price,act,why,sep = ' | ')