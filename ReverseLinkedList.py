
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None

    def addNode(self, node):
        if not self.root:
            self.root = node

        elif not self.root.next:
            self.root.next = node

        else:
            trav = self.root
            while trav.next != None:
                trav = trav.next
            trav.next = node

    def reverseList(self, head):
        prevNode = head
        currNode = head
        nextNode = head.next

        while nextNode:
            currNode = nextNode
            nextNode = currNode.next

            currNode.next = prevNode
            prevNode = currNode

        head.next = None
        return currNode

    def deleteNode(self, node):
        travNode = self.root

        while travNode.next.val != node.val:
            travNode = travNode.next

        travNode.next = node.next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
       # prev = 


s = Solution()
n1,n2,n3,n4,n5 = Node(1),Node(2),Node(3),Node(4),Node(5)
nodeList = [n1,n2,n3,n4,n5]

l = LinkedList()
for node in nodeList:
    l.addNode(node)

#l.reverseList(n1)
l.deleteNode(n4)
print("hola")

