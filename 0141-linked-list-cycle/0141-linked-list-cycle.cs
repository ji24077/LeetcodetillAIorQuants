/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public bool HasCycle(ListNode head) {
      
      //set to store  is it visted node.
      //everytime if u visted the node, double check from visted node. for already visited.-> thats a cycle.

      HashSet<ListNode> visited = new HashSet<ListNode>();

      while ( head != null){
        if(visited.Contains(head)){
          return true;
        }
        visited.Add(head); // mark as visted.
        head = head.next;

      }
      return false; // no cycle.
        
    }
}