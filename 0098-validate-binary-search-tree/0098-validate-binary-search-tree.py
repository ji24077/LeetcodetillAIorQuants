class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_val, max_val):
            if not node:
                return True
            
            # 현재 노드가 BST 조건을 만족하지 않으면 False
            if not (min_val < node.val < max_val):
                return False
            
            # 왼쪽은 max를 현재 노드보다 작게, 오른쪽은 min을 현재 노드보다 크게
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        return dfs(root, float('-inf'), float('inf'))
