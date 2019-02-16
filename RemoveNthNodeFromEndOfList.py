# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList():
    head = None
    def addNodeToLinkedList(self,node):
        #1st node
        if not self.head:
            self.head = node
        #2nd node
        elif not self.head.next:
            self.head.next = node
        #rest of the nodes
        else:
            tmp = self.head
            #traverse to the end using tmp node
            while tmp.next:
                tmp = tmp.next
            tmp.next = node

    def printLinkedList(self,head):
        tmp = head 
        while tmp:
            print("{0}  ".format(tmp.val))
            tmp = tmp.next

class Solution():
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        lengthOfLinkedList = 0
        tmp = head
        while tmp:
            lengthOfLinkedList += 1
            tmp = tmp.next
        
        if lengthOfLinkedList == 1 and n ==1:
            head = None
            return head
        
        #preceding node to the one to be removed
        lengthToTravere = lengthOfLinkedList-n
        i=1
        
        tmp = head
        while i < lengthToTravere:
            tmp = tmp.next
            i += 1
        
        #tmp holds the node just before the node to be removed
        #tmp2 is the node to be removed
        if tmp == head:
            #head node is to be removed
            if lengthToTravere == 0:
                head = tmp.next
                return head

        tmp2 = tmp.next
        tmp.next = tmp2.next
        return head

#create nodes 
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

#add nodes to linked list
l = LinkedList()
l.addNodeToLinkedList(n1)
l.addNodeToLinkedList(n2)
l.addNodeToLinkedList(n3)
l.addNodeToLinkedList(n4)
l.addNodeToLinkedList(n5)

s = Solution()

#print list
l.printLinkedList(s.removeNthFromEnd(n1,2))
