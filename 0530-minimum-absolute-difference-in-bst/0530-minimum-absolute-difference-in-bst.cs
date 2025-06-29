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

    private int minDiff = int.MaxValue;
    private TreeNode prev = null; // inroder traveral.

    public int GetMinimumDifference(TreeNode root) {
      //int mindiff = inf;
      // TreeNode prev
      // inorder(root); u can update mindiff inside of the fcn.
     

      Inorder(root);

      return minDiff;

      

        
    }
    private void Inorder(TreeNode root){
        if(root == null){
          return;
        }
        Inorder(root.left);
        if(prev != null){
          int diff = root.val - prev.val;
          minDiff = Math.Min(minDiff, diff);
        }
        prev = root;
        Inorder(root.right);

      }
}