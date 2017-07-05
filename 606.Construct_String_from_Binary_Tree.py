# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t == None:
            return ""
        return self.loop(t)
    
    def loop(self,t):
        if t.left == None and t.right == None:
            return str(t.val)
        elif t.left == None and t.right!=None:
            return str(t.val)+"()("+self.loop(t.right)+")"
        elif t.right == None and t.left!=None:
            return str(t.val)+"("+self.loop(t.left)+")"
        else:
            return str(t.val)+"("+self.loop(t.left)+")("+self.loop(t.right)+")"
        
            
