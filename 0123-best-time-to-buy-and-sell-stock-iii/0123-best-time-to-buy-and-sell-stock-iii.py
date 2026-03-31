class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      if not prices or len(prices) < 2:
        return 0 # if only one day or list is empty then return 0

      #first buy and max state, we bought stock, so it has to be negative state

      first_buy = -prices[0]

      #max profit after first sell, since initailly its 0

      first_sell = 0 # sell nothing

      second_buy = -prices[0]
      second_sell = 0

      #now we have to traverse all 4 state, and record / update theses two states

      for price in prices:
        first_buy = max(first_buy, - price) #compare original price and today's
        first_sell = max(first_sell, first_buy + price) # similarly

        second_buy = max(second_buy, first_sell - price) # we pay as much as first_sell profit - price

        second_sell = max(second_sell, second_buy + price) # similarly
        result = second_sell
      return result