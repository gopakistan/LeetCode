# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """


        temp = head
        tempDelay = head
        i = 0
        while temp.next is not None:
            temp = temp.next
            i += 1
            if i > n:
                tempDelay = tempDelay.next
        print(str(tempDelay.val), str(n), str(i))
        if i == 0:
            return None
        if i + 1 == n:
            return head.next
        if n >= 2:
            tempDelay.next = tempDelay.next.next
        elif n == 1:
            tempDelay.next = None        


        return head
