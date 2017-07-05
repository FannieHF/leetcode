# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.row = []
        self.tree = []   
        if root == None:
            return self.row
        
        self.tree.append(root.val)
        self.loop(0,root)
        print self.tree
        return self.row
        
        
    def loop(self,index,root):
        if len(self.row) <= index:
            self.row.append(root.val)
        else:
            self.row[index] = max(root.val,self.row[index])
        if root.left != None:
            self.tree.append(root.left.val)
            self.loop(index+1,root.left)
        if root.right != None:
            self.tree.append(root.right.val)
            self.loop(index+1,root.right)
        if self.tree[-1] == root.val:
            return

