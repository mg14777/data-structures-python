import datastructures.binary_search_tree as program
import unittest

test1 = program.BST(10).insert(5).insert(15).insert(5).insert(2).insert(14).insert(22)

test2 = program.BST(10).insert(15).insert(11).insert(22).remove(10)

test3 = program.BST(10).insert(5).insert(7).insert(2).remove(10)

test4 = program.BST(10).insert(5).insert(15).insert(22).insert(17).insert(34) \
.insert(7).insert(2).insert(5).insert(1).insert(35).insert(27).insert(16) \
.insert(30).remove(22).remove(17)

def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


class TestProgram(unittest.TestCase):

	def test_case_1(self):
		self.assertEqual(test1.left.value, 5)

	def test_case_2(self):
		self.assertEqual(test1.right.right.value, 22)

	def test_case_3(self):
		self.assertEqual(test1.right.left.value, 14)

	def test_case_4(self):
		self.assertEqual(test1.left.right.value, 5)

	def test_case_5(self):
		self.assertEqual(test1.left.left.value, 2)

if __name__ == "__main__":
	unittest.main()