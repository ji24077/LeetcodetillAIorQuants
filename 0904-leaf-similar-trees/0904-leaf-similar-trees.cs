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
    public bool LeafSimilar(TreeNode root1, TreeNode root2) {
      List<int> leaf1 = new List<int>();
      List<int> leaf2 = new List<int>();
      getLeaf(root1, leaf1);
      getLeaf(root2, leaf2);
      if( leaf1.Count != leaf2.Count){
        return false;
      }
      //since order doesnt matter,
      for(int i = 0; i < leaf1.Count; i++){
        if(leaf1[i] != leaf2[i]){
          return false;
        }
      }
      return true;

      
    }
    private void getLeaf(TreeNode root, List<int> leaf){
        if(root == null){
          return;
        }
        if(root.left == null && root.right == null){
          leaf.Add(root.val);
          return;
        }
        getLeaf(root.left, leaf);
        getLeaf(root.right, leaf);

      }
}





