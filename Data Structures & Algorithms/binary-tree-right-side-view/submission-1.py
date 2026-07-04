# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return []
        queue=deque()
        ans=[]
        queue.append([root,1])
        res={}
        while queue:
            e,level=queue.popleft()
            if level not in res:
                res[level]=[e.val]
            else:
                res[level].append(e.val)

            if e.right:
                queue.append([e.right,level+1])
            if e.left:
                queue.append([e.left,level+1])
        for val in sorted(res.items()):
            ans.append(val[1][0])
        return ans
            
        