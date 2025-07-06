// public class Solution {
//     public int MaxProfit(int[] prices) {

        
//     }
// }
public class Solution{
  public int MaxProfit(int[] prices){
    //we make profit when price[i] > price[i-1]
    //since we buy price at i-1, and sell at price[i].

    int profit = 0;
    for(int i = 1; i < prices.Length; i++){
      if( prices[i] > prices[i-1]){
        profit += prices[i] - prices[i -1];
      }
    }
    return profit;
  }
}