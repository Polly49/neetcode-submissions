# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count=0
        if not root:
            return 0

        def cnt(node,mx):
            if not node:
                return self.count

            if node.val>=mx:
                self.count+=1
                
            mx=max(node.val,mx)
            
            cnt(node.left,mx)
            cnt(node.right,mx)
            return self.count

        a=cnt(root,root.val)
        return a

