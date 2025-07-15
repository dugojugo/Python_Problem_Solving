# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i+1 < len(lists) else None
                temp.append(self.mergeLists(l1,l2))
            lists = temp
        return lists[0]
    def mergeLists(self, l1: Optional[ListNode],l2: Optional[ListNode]):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            val1 = l1.val
            val2 = l2.val

            if val1 > val2:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
                
            curr = curr.next

        if l1:
            curr.next = l1
        else:
            curr.next = l2

        return dummy.next


def main():
    node1 = ListNode(1, ListNode(4, ListNode(5)))
    node2 = ListNode(1, ListNode(3, ListNode(4)))
    node3 = ListNode(2, ListNode(6))
    lists = [node1, node2, node3]
    solution = Solution()
    merged = solution.mergeKLists(lists)
    while merged:
        print(merged.val, end=" -> ")
        merged = merged.next
   
    print("None")

if __name__ == "__main__":
    main()
