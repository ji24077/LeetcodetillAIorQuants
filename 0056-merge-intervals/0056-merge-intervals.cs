public class Solution{
  public int[][] Merge(int[][] intervals){
    //sort based on start.
    //if start  is overlaps with first intervals, merge.

    //intervals.Sort(based onstart),
    //result = {};
    //foreach(var interval in intervals){ if result is empty or not overlaps.
    // u add result.Add(interval) //new intevval
    //ow jsut updtte, merge whch updtate end index.
    Array.Sort(intervals, (a, b) => a[0].CompareTo(b[0]));

    List<int[]> result = new List<int[]>();

    foreach(int[] interval in intervals){
      if(result.Count == 0 || result.Last()[1] < interval[0]){
        //ur end of 2nd interval is smaler than first interval's start.
        result.Add(interval);
      }
      else{ // overlaps.
        // if( interval[1] < result.Last()[1])
        // {
        //   result.Last()[1] = result.Last()[1]
        // }
        result.Last()[1] = Math.Max(result.Last()[1], interval[1]);

      }
    }
    return result.ToArray();

  }
}