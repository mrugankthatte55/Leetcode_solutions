# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        result = [None] * k
        total_nodes = 0
        current_node = head
        
        while current_node:
            total_nodes += 1
            current_node = current_node.next

        base_size = total_nodes // k
        extra_nodes = total_nodes % k

        current_node = head
        for i in range(k):
            part_head = current_node
            part_size = base_size + (1 if extra_nodes > 0 else 0)
            if extra_nodes > 0:
                extra_nodes -= 1
            
            prev_node = None
            for j in range(part_size):
                prev_node = current_node
                if current_node:
                    current_node = current_node.next

            if prev_node:
                prev_node.next = None
            
            result[i] = part_head

        return result
