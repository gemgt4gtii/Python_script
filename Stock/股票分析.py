import twstock
stock = twstock.Stock('2345')
print(stock.moving_average(stock.price,5))