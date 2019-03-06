import twstock
stock = twstock.Stock('2345')
bfp = twstock.BestFourPoint(stock)
print(bfp.best_four_point())