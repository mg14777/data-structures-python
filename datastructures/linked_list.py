class Node:

	def __init__(self, val, next=None):
		self.val = val
		self.next = next

	def __str__(self):
		return self.val

class SinglyLinkedList:

	def __init__(self, head=None):
		self.head = head
		self.size = 1 if self.head else 0

	def __len__(self):
		return self.size

	def __iter__(self):
		current = self.head
		while current:
			data = current.val
			current = current.next
			yield data

	def __str__(self):
		return '->'.join([str(data) for data in iter(self)])

	def append(self, val):
		''' Adds an element to the end of the list '''
		new_node = Node(val)
		if self.head is None:
			self.head = new_node
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = new_node
		self.size += 1

	def insert_to_front(self, val):
		''' Adds an element to beginning of the list '''
		new_node = Node(val)
		new_node.next = self.head
		self.head = new_node
		self.size += 1

	def find(self, val):
		''' Find the linked list node given its value '''
		current = self.head
		while current and current.val != val:
			current = current.next
		return current

	def delete(self, val):
		''' Delete a node given its value '''
		if self.head:
			return
		if self.head.val == val:
			self.head = self.head.next
			return
		current = self.head
		sentinel = Node(-1, self.head)
		while current:
			if current.val == val:
				sentinel.next = current.next
				return
			current = current.next
			sentinel = sentinel.next
		return


if __name__ == '__main__':
	n1 = Node(2)
	ll = SinglyLinkedList(n1)
	print('After initialization') 
	print(ll)
	
	ll.append(3)
	ll.append(4)
	ll.append(6)
	print('After appending 3, 4 and 6')
	print(ll)

	ll.insert_to_front(5)
	print('After inserting 5 at beginning')
	print(ll)

	elems = [1,3,5,6,9]
	for elem in elems:
		print('Node with value {0} exists: {1}'.format( elem, bool(ll.find(elem)) ) )

	ll.delete(5)
	print('After deleting head: 5')
	print(ll)

	ll.delete(3)
	print('After deleting mid: 3')
	print(ll)

	ll.delete(6)
	print('After deleting end: 6')
	print(ll)
