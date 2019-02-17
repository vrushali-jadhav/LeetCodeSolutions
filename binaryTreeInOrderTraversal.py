# Definition for a binary tree node.
class TreeNode():
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class BinaryTree():
    root = None
    q = []
    def addNode(self,node):
        #add 1st node
        if not self.root:
            self.root = node
            self.q.append(self.root)
            return None

        if not self.q[0].left:
            self.q[0].left = node
            self.q.append(node)
        elif not self.q[0].right:
            self.q[0].right = node
            self.q.append(node)
            self.q.pop(0)
        
class Solution():
    inorderTree = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.inorderTraversalRecursive(root)
        return self.inorderTree

    def inorderTraversalRecursive(self,root):
        if root:
            if root.left or root.right:
                self.inorderTraversalRecursive(root.left)
                self.inorderTree.append(root.val)
                self.inorderTraversalRecursive(root.right)
                
        #if leaf node
        if root:
            if not root.right and not root.left:
                self.inorderTree.append(root.val)
        
        
#create tree nodes 
t1 = TreeNode(1)
t2 = TreeNode(3)
t3 = TreeNode(6)
t4 = TreeNode(2)
t5 = TreeNode(8)
t6 = TreeNode(0)
t7 = TreeNode(4)
t8 = TreeNode(9)
t9 = TreeNode(10)
t10 = TreeNode(11)
t11 = TreeNode(12)
t12 = TreeNode(13)
t13 = TreeNode(14)
t14 = TreeNode(15)
t15 = TreeNode(16)

b = BinaryTree()
b.addNode(t1)
b.addNode(t2)
b.addNode(t3)
b.addNode(t4)
b.addNode(t5)
b.addNode(t6)
b.addNode(t7)
b.addNode(t8)
b.addNode(t9)
b.addNode(t10)
b.addNode(t11)
b.addNode(t12)
b.addNode(t13)
b.addNode(t14)
b.addNode(t15)

s = Solution()
print(s.inorderTraversal())
 