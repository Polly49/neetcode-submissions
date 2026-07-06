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
            self.a.add(node.val)
            self.ans.append(node.val)
            solve(node.right)
            if node.val not in self.a:
                self.ans.append(node.val)
            
            return self.ans
        solve(root)
        return self.ans[k-1]


        