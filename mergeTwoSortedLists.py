# Definition for singly-linked list.
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

    def createLinkedList(self,listOfNodes):
        headNode = listOfNodes[0]
        traverseNode = headNode
        for node in listOfNodes[1:]:
            traverseNode.next = node
            traverseNode = node

    def printLinkedList(self,firstNode):
        headNode = firstNode
        traverseNode = headNode
        
        print("\nLinked list:")
        while traverseNode:
            print("{0}".format(traverseNode.val))
            traverseNode = traverseNode.next

class Solution():
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        listToReturn = ListNode(0)
        head = listToReturn
        while l1 and l2:
            if l1.val < l2.val:
                listToReturn.next = l1
                l1 = l1.next
            else:
                listToReturn.next = l2
                l2 = l2.next
            listToReturn = listToReturn.next
        if l2:
            listToReturn.next = l2
        elif l1:
            listToReturn.next = l1 
        return head.next

#form list one
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(4)

l1.createLinkedList([l1,l2,l3])
#l1.printLinkedList(l1)

#form list two
l4 = ListNode(1)
l5 = ListNode(3)
l6 = ListNode(4)

l4.createLinkedList([l4,l5,l6])
#l4.printLinkedList(l4)

s = Solution()
l1.printLinkedList(s.mergeTwoLists(l1,l4))

