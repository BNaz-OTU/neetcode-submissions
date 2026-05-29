class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        
        def dfs(root):
            nonlocal max_diameter

            if (root is None):
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            
            max_diameter = max(max_diameter, left + right)
            
            return max(left, right) + 1
        
        dfs(root)

        return max_diameter