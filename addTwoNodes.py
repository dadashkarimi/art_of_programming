# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import operator

def addTwoNodes(node1,node2,overflow):
    sum_ = node1.val + node2.val+overflow
    # print(node1.val,node2.val,sum_)
    if sum_ >= 10:
        sum_ = sum_ - 10
        overflow = 1
        print(sum_)
        node = ListNode(sum_, ListNode(overflow,None))
    else:
        overflow = 0
        node = ListNode(sum_, None)
        
    node1 = node1.next
    node2 = node2.next

    return node,node1,node2, overflow

class Solution(object):
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        node,l1,l2, overflow = addTwoNodes(l1,l2,0)
        first_node = node
        i = 0 
        
        while(not l1 is None or not l2 is None):
            
            if l2 is None:
                l2 = ListNode(0,None)
            
            if l1 is None:
                l1 = ListNode(0,None)
                
            next_node, l1,l2, overflow = addTwoNodes(l1,l2,overflow)
            if i ==0:
                first_node.next = next_node
            else:
                node.next = next_node
                
            node = next_node
            i = i + 1
            
        return first_node
        
