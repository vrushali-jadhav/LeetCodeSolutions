class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        if not root:
            return True
        if not root.left and not root.right:
            return True
        elif root.left and root.right:
            if root.left.val == root.right.val:
                stack.append(root.left)
                stack.append(root.right)
                #we need a tmp stack for storing all the root on the same level
                tmpStack = []
                while(stack):
                    #we are taking 1st and last root from the stack for comparision
                    l_root = stack.pop(0)
                    r_root = stack.pop()
                    if not tmpStack:
                        tmpStack.append(l_root)
                        tmpStack.append(r_root)
                    else:
                        #a child of a node should be added in the middle (like how tree would look)
                        ind = len(tmpStack)/2
                        tmpStack.insert(ind, l_root)
                        tmpStack.insert(ind+1, r_root) 
                    #leaf node
                    if not l_root.left and not r_root.left and not l_root.right and not r_root.right:
                        return True
                    
                    if (not l_root.left and r_root.right) or (l_root.left and not r_root.right):
                        return False
                    elif l_root.left and r_root.right:
                        if l_root.left.val != r_root.right.val:
                            return False

                    if (not l_root.right and r_root.left) or (l_root.right and not r_root.left):
                        return False                
                    elif l_root.right and r_root.left:
                        if l_root.right.val != r_root.left.val:
                            return False
                    #add nodes to the stack only if it is non-null
                    if not stack:
                        while(tmpStack):
                            root = tmpStack.pop(0)
                            if root.left:
                                stack.append(root.left)
                            if root.right:
                                stack.append(root.right)
            else:
                return False
        else:
            return False

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