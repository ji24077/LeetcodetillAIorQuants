/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public IList<double> AverageOfLevels(TreeNode root) {
      //List<doubl> ;
      //if root ==null-> return false;
      //Queue<TreeNode> q = new..
      //q.Enqueue(root)
      //while( q.count> 0){ calculate avg based on level}

      List<double> result = new List<double>();

      // if (root == null){
      //   return result;
      // }
      Queue<TreeNode> q = new Queue<TreeNode>();

      q.Enqueue(root);
      //this is where we going to start BFS.
      while(q.Count > 0){
        int levelCount = q.Count; // at first its 1.
        double levelSum = 0;

        for(int i = 0; i < levelCount; i++){
          TreeNode curr = q.Dequeue();
          levelSum += curr.val;
          if(curr.left != null){
            q.Enqueue(curr.left);
          }
          if(curr.right != null){
            q.Enqueue(curr.right);
          }
        }
        double sumAvg = levelSum/levelCount;
        result.Add(sumAvg);


      }
      return result;
      


        
    }
}