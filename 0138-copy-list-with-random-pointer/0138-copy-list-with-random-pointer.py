"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # ✅ 예외 처리: 빈 리스트면 그대로 반환
        if not head:
            return None

        # ✅ 1단계: 원본 노드 -> 복사 노드 매핑 저장용 딕셔너리
        old_to_new = {}  # ➡️ {원본노드: 새노드}

        # ✅ 2단계: 첫 번째 순회에서 새 노드를 만들기만 하고 매핑 기록
        current = head
        while current:
            # ➡️ 같은 값으로 새 노드 생성 (next, random은 아직 연결 안 함)
            old_to_new[current] = Node(current.val)
            current = current.next

        # ✅ 3단계: 두 번째 순회에서 매핑을 활용해 next, random 연결
        current = head
        while current:
            # ➡️ 현재 복사 노드 가져오기
            copy_node = old_to_new[current]
            # ➡️ next 포인터 복사: 원본의 next가 있다면 매핑된 새 노드로 연결
            copy_node.next = old_to_new.get(current.next)
            # ➡️ random 포인터 복사: 원본의 random이 있다면 매핑된 새 노드로 연결
            copy_node.random = old_to_new.get(current.random)
            current = current.next

        # ✅ 4단계: head에 해당하는 복사 노드를 반환
        return old_to_new[head]