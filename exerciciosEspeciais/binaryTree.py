class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            # Update the diameter if the sum of left and right depths is greater
            self.diameter = max(self.diameter, left_depth + right_depth)
            # Return the depth of the current node's subtree
            return 1 + max(left_depth, right_depth)

        dfs(root)
        return self.diameter

# Example usage:
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

solution = Solution()
print(solution.diameterOfBinaryTree(root1))  # Output: 3

root2 = TreeNode(1)
root2.left = TreeNode(2)

print(solution.diameterOfBinaryTree(root2))  # Output: 1
