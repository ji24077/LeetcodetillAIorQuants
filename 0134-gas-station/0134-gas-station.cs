public class Solution {
    public int CanCompleteCircuit(int[] gas, int[] cost) {
      int totalTank = 0; // comparing as total < 0 -> return -1
      int currTank = 0;
      int start = 0;
      for(int i = 0; i < gas.Length; i++){
        int diff = gas[i] - cost[i]; // bc we need to check is it neg.
        currTank += diff; 
        totalTank += diff; // this will explain is total cost < gas.

        if(currTank < 0){
          start = i + 1;
          currTank = 0;

        }
      }
      return totalTank < 0 ? -1 : start;

        
    }
}