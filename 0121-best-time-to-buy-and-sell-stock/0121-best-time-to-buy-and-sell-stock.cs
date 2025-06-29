public class Solution {
    public int MaxProfit(int[] prices) {
      int maxProfit = 0;
      int minPrice = int.MaxValue;
      //for price in prices: keep update the min price;
      //if  price < minPrice : minprice = price;
      //ow: its the min priace, and maxprofit,
      //profit = price - minPrice;
      // maxProfit = Math.Max(maxProfix, profit);
      //after, u just returm max;

      foreach(int price in prices ){
        if( price < minPrice){
          minPrice = price; // keep tracking the minPrice;
        }
        else{
          int profit = price - minPrice;

          maxProfit = Math.Max(maxProfit, profit);

        }
      }
      return maxProfit;


        
    }
}