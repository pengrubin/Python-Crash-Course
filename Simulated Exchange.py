class Exchange:
    def __init__(self):
        pass
        self.id=0
        self.side=[]
        self.volume=[]
        self.price=[]


    def InputOrder(self, side, volume, price):
        """
        InputOrder receives order, and return assigned order Id.
        :param side: 0 is buy, 1 is sell,-1 means not valid
        :param volume:order's quantity
        :param price:order's prices
        :return: order Id, an integer
        """
        self.side.append(side)
        self.volume.append(volume)
        self.price.append(price)
        self.id+=1
        return self.id

    def QueryOrderTrade(self, orderId):
        """
        queries order's trade volume and average price.
        :param orderId: assigned order Id
        :return: (order's trade volume, avg_price),tuple
        """
        volume = self.volume[int(orderId)-1]
        avg_price = self.price[int(orderId)-1]/self.volume[int(orderId)-1]
        return (volume, avg_price)

if __name__ == "__main__":
    ex = Exchange()
    orders = list()

    orders.append(ex.InputOrder(0, 1, 100))
    orders.append(ex.InputOrder(0, 2, 101))
    orders.append(ex.InputOrder(0, 3, 102))
    orders.append(ex.InputOrder(1, 4, 100))
    orders.append(ex.InputOrder(1, 5, 101))
    orders.append(ex.InputOrder(1, 6, 102))

    for orderId in orders:
        tradeVolume, avgPrice = ex.QueryOrderTrade(orderId)
        print("orderId:%d,tradeVolume:%d,averagePrcies:%f"%(orderId, tradeVolume, avgPrice))


