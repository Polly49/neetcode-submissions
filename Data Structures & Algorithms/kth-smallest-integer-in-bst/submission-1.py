# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans=[]
        self.a=set()
        def solve(node):
            if node is None :
                return self.ans
            solve(node.left)
            self.ans.append(node.val)
            solve(node.right)
            return self.ans
        solve(root)
        return self.ans[k-1]


        