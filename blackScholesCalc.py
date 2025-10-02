import math
from scipy.stats import norm

class BlackScholesCalc:
    def __init__(self,S, K, T, r, vol):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.vol = vol
        self.d1 = (math.log(self.S / self.K) + (self.r + self.vol ** 2 * 0.5) * self.T) / (self.vol * math.sqrt(self.T))
        self.d2 = (self.d1 - (self.vol * math.sqrt(self.T)))
        self.C = (self.S * norm.cdf(self.d1) - self.K * math.exp(-self.r * self.T) * norm.cdf(self.d2))
        self.P = (self.K * math.exp(-self.r * self.T) * norm.cdf(-self.d2) - self.S * norm.cdf(-self.d1))

    def getCall(self):
        return self.C

    def getPut(self):
        return self.P

