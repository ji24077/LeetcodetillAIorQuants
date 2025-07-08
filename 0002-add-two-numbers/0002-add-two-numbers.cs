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
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
      // 결과 리스트의 시작을 쉽게 하기 위해 dummy 노드 사용
        ListNode dummy = new ListNode(0); 
        ListNode curr = dummy; // 결과 연결 리스트의 현재 노드
        int carry = 0; // 자리올림 값 저장

        // 두 리스트 모두 null이 아닐 때까지 반복
        while (l1 != null || l2 != null) {
            int x = (l1 != null) ? l1.val : 0; // l1 값이 있으면 가져오고, 없으면 0
            int y = (l2 != null) ? l2.val : 0; // l2 값도 마찬가지
            int sum = x + y + carry; // 현재 자릿수의 합

            carry = sum / 10; // 10 이상이면 자리올림 발생
            curr.next = new ListNode(sum % 10); // 현재 자릿수 노드 생성
            curr = curr.next; // 포인터 이동

            if (l1 != null) l1 = l1.next; // 다음 노드로 이동
            if (l2 != null) l2 = l2.next;
        }

        // 모든 노드를 처리한 후에도 자리올림이 남아있으면 새 노드 추가
        if (carry > 0) {
            curr.next = new ListNode(carry); // 조건적으로 필요
        }

        return dummy.next; // dummy 다음 노드가 결과 리스트의 시작
        
    }
}