
class Node:

	def __init__(self, val, next=None):
		self.val = val
		self.next = next

'''
Given a pointer to the start of a linked list
with a circle,
find out the first place where the circle starts.

length of string section: k nodes
length of cycle: n nodes

 0
 |
 V
 1 
 |
 V
 2
 |
 V
 3 -> 4
 ^    |
 |    V
 6 <- 5
       slow,fast

when slow has moved x nodes, thus being m nodes into the start of the cycle,
fast has moved 2x nodes.

When they meet, they meet at a position of p nodes into the cycle,
then slow has travelled x nodes and fast has travelled 2x nodes.
Then k + p = x 



POINTER_1
 0
 |
 V
 1 
 |
 V
 2
 |
 V
 3 -> 4
 ^    |
 |    V
 6 <- 5
      POINTER_2

'''


def return_cycle_start(node):
	slow = node
	fast = node
	while fast.next and fast.next.next:
		slow = slow.next
		fast = fast.next.next
		if slow == fast:




