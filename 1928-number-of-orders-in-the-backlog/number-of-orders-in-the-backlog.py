class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy = []
        sell = []

        for order in orders:
            price, amt, orderType = order

            if orderType == 0:
                while sell and price >= sell[0][0] and amt > 0:
                    if amt >= sell[0][1]:
                        amt -= sell[0][1]
                        heapq.heappop(sell)
                    else:
                        old_order = heapq.heappop(sell)
                        heapq.heappush(sell, (old_order[0], old_order[1] - amt))
                        amt = 0
                    
                if amt > 0:
                    heapq.heappush(buy, (-price, amt))
            else:
                while buy and price <= -buy[0][0] and amt > 0:
                    if amt >= buy[0][1]:
                        amt -= buy[0][1]
                        heapq.heappop(buy)
                    else:
                        old_order = heapq.heappop(buy)
                        heapq.heappush(buy, (old_order[0], old_order[1] - amt))
                        amt = 0
                
                if amt > 0:
                    heapq.heappush(sell, (price, amt))

        orders = 0
        for ele in buy:
            orders += ele[1]
        for ele in sell:
            orders += ele[1]
        
        return orders % (10 ** 9 + 7)