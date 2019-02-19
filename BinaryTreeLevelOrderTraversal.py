# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree():
    root = None
    treeNodeQueue = []

    def addNode(self, node):

        #root node
        if not self.root:
            self.root = node
            self.treeNodeQueue.append(self.root)
        
        #1st left node
        else:
            if not self.treeNodeQueue[0].left:
                self.treeNodeQueue[0].left = node
                self.treeNodeQueue.append(node)
              
            #1st right node, remove the current root node from the queue as it has both the child
            elif not self.treeNodeQueue[0].right:
                self.treeNodeQueue[0].right = node
                self.treeNodeQueue.append(node)
                self.treeNodeQueue.pop(0)


class Solution():
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #this list holds the lists of nodes
        levelOrderList = []
        #this is siblings list
        siblings = []
        #this holds values of siblings
        siblingValues = []
        #list of list of sibling values
        finalValues = []

        if not root:
            return []
        else:
            levelOrderList.append([root])
            finalValues.append([root.val])
           
        i = 0
        for listOfNodes in levelOrderList:
            siblings = []
            siblingValues = []
            for curr_root in listOfNodes: 
                if curr_root.left:
                    siblings.append(curr_root.left)
                    siblingValues.append(curr_root.left.val)
                if curr_root.right:
                    siblings.append(curr_root.right)
                    siblingValues.append(curr_root.right.val)
        
            if siblings:
                levelOrderList.append(siblings)
                finalValues.append(siblingValues)

        return finalValues

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
print(s.levelOrder(t1))