# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        temp=root
        ans=[]
        a=set()
        while temp is not None:
            a.add(temp.val)
            if temp.val==p.val:
                a.add(temp.val)
                break
            elif temp.val < p.val:
                temp=temp.right 
            else:
                temp=temp.left
        temp = root
        while temp is not None:
            if temp.val in a:
                ans.append(temp)
            if temp.val==q.val:
                break
            elif temp.val<q.val:
                temp=temp.right 
            else:
                temp=temp.left
        return ans[-1]


