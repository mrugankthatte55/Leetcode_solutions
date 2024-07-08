# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        h=head
        d={}
        i=0
        while h:
            if h.val in d:
                d[h.val].append(i)
            else:
                d[h.val]=[i]
            h=h.next
            i+=1
        h=ListNode
        h.next=head
        f=0
        for i in d:
            if len(d[i])==1:
                f=1
                h=h.next
                print(i)
                h.val=i
        if f==0:
            head=None
            return head
        h.next=None
        print(d)
        return head