/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        //oHead pointer where store the new node (0)
        //curr = newnode(0)
        //while(list1.next != null && list2.next != null)
        //if(list1.val is greater){ curr.next = list1 , and keep move}
        //similarly for other case
        // u look curr too.
        //make sure you connect the rest remained list for list1,2


        ListNode dummy = new ListNode(0); // null head.

        ListNode curr = dummy;


        while(list1 != null && list2 != null ){
          if(list1.val < list2.val){
            curr.next = list1;
            list1 = list1.next;
          }
          else{ // list1.val<list2.val
            curr.next = list2;
            list2 = list2.next;
          }
          curr = curr.next;
        }

        //the lenfth of the both side is not same.
        //so the thing is, since its given to be sorted, I can just connect the next remained tail from curr.

        if( list1 != null){
          curr.next = list1;
        }
        if( list2 != null){
          curr.next = list2;
        }
        return dummy.next;
    }
}