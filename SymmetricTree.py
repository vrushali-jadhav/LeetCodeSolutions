class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        if not root:
            return True
        
        stack.append(root.left)
        stack.append(root.right)

        while(stack):
            l, r = stack.pop(), stack.pop()
            # dont check for roots right and left child already. If they are none, add them still
            # this condition will atek of them being none
            if not l and not r:
                continue
            # you had this problem where you were checking value of none nodes. It was erroring out 
            # this takes care of that situation. 
            # if both are none, that fine. But its not a mirror image if just one of them is none.
            if (not l) or (not r) or (l.val !=r.val) :
                return False
                
            stack.append(l.left)
            stack.append(r.right)
            stack.append(l.right)
            stack.append(r.left)

        return True
        
class Tree:
    root = None
    stackOfRoots = []
    def insertNode(self, node):
        #if root is NULL, make the node root
        if not self.root:
            self.root = node
            self.stackOfRoots.append(self.root)
        else:
            self.traverseTree(node)

    def traverseTree(self, node):
        while(self.stackOfRoots):
            root = self.stackOfRoots[0]
            if not root.left:
                root.left = node
                break
            if not root.right:
                root.right = node
                break
            #root needs to be changed
            if root.left and root.right:
                self.stackOfRoots.append(root.left)
                self.stackOfRoots.append(root.right)
                self.stackOfRoots.pop(0)

    def displayTree(self, root):
        print(root.val)
        stack = []
        stack.append(root)

        while(stack):
            root = stack[0]
            if root.left:
                print(root.left.val)
            if root.right:
                print(root.right.val)
            #root needs to be changed
            if root.left and root.right:
                stack.append(root.left)
                stack.append(root.right)
                stack.pop(0)
            if not root.left and not root.right:
                break
    
class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

s = Solution() 
t = Tree()

n1 = Node(1)
n2 = Node(2)
n3 = Node(2)
n4 = Node(None)
n5 = Node(3)
n6 = Node(3)
n7 = Node(4)
n8 = Node(6)
n9 = Node(None)
n10 = Node(8)
n11 = Node(9)
n12 = Node(9)
n13 = Node(8)
n14 = Node(None)
n15 = Node(6)
#n7 = Node(3)

t.insertNode(n1)
t.insertNode(n2)
t.insertNode(n3)
t.insertNode(n4)
t.insertNode(n5)
t.insertNode(n6)
#t.insertNode(n7)
#t.insertNode(n8)
#t.insertNode(n9)
#t.insertNode(n10)
#t.insertNode(n11)
#t.insertNode(n12)
#t.insertNode(n13)
#t.insertNode(n14)
#t.insertNode(n15)
#t.insertNode(n7)

#t.displayTree(n1)
#[1,2,2,null,3,3]
print(s.isSymmetric(n1))
#[2,3,3,4,5,5,4,null,null,8,9,9,8]
#([1,2,2,3,4,4,3])