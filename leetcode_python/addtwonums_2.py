class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        str1 , str2 = '' , ''
        while l1:
            str1 += str(l1.val)
            l1 = l1.next
        while l2:
            str2 += str(l2.val)
            l2 = l2.next
        int1 = int(str1[::-1])
        int2 = int(str2[::-1])
        return list(map(int,str(int1+int2)[::-1]))


