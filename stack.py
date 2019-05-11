class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

	def __str__(self):
		return self.val


class Stack:
	def __init__(self, top=None):
		self.top = top
		self.size = 1 if self.top else 0

	def __len__(self):
		return self.size

	def push(self, val):
		''' Push element to top of stack '''
		if not self.top:
			self.top = Node(val)
			self.size += 1
			return
		new_top = Node(val)
		new_top.next = self.top
		self.top = new_top
		self.size += 1

	def pop(self):
		''' Pop element from top of stack '''
		if not self.top:
			raise Exception('Cannot pop from an empty stack...')
		top_val = self.top.val
		self.top = self.top.next
		self.size -= 1
		return top_val

	def peek(self):
		''' Return element from top of stack '''
		if self.top:
			return self.top.val

if __name__ == '__main__':

	stack = Stack()

	print('Push elements to stack: 34, 35, 36')
	stack.push(34)
	stack.push(35)
	stack.push(36)

	print('Length of stack')
	print(len(stack))

	print('Peek at the top element')
	print(stack.peek())

	print('Pop the top element')
	print(stack.pop())

	print('Peek again')
	print(stack.peek())

	print('Pop remaining 2 elements')
	print(stack.pop())
	print(stack.pop())

	print('Peek an empty stack')
	print(stack.peek())

	print('Length of stack')
	print(len(stack))

	print('Pop an empty stack')
	print(stack.pop())
