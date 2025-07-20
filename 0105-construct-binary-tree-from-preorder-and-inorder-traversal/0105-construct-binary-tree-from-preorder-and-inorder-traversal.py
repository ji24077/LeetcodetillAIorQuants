# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 중위 순회 값 -> 인덱스 매핑 (빠른 조회)
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        
        # 전위 순회의 현재 위치를 추적할 포인터
        self.pre_idx = 0
        
        # 재귀 함수: inorder 구간 [left, right]에 해당하는 서브트리 생성
        def helper(left: int, right: int) -> Optional[TreeNode]:
            # 범위를 벗어나면 서브트리 없음
            if left > right:
                return None
            
            # 전위 순회에서 현재 루트 값 선택
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            
            # 루트 노드 생성
            root = TreeNode(root_val)
            
            # 중위 순회에서 루트 값의 인덱스 찾기
            mid = idx_map[root_val]
            
            # 왼쪽 서브트리 생성
            root.left = helper(left, mid - 1)
            # 오른쪽 서브트리 생성
            root.right = helper(mid + 1, right)
            
            return root
        
        # 전체 inorder 범위에 대해 재귀 시작
        return helper(0, len(inorder) - 1)