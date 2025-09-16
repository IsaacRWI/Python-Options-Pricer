import math
import scipy

S = 42  # underlying price ie price of stock rn
K = 40  # strike price ie right to buy the stock at $
T = 0.5  # time to expiration ie when the option expires (years)
r = 0.04  # risk-free returns (percentage as a number) ex: uk treasury bill returns
vol = 0.2  # volatility ie standard deviation for stock (percentage as a number)

# black scholes calculations
d1 = (math.log(S/K) + (r + vol**2 * 0.5) * T) / (vol * math.sqrt(T))
print(d1)
d2 = (d1 - (vol * math.sqrt(T)))
print(d2)

