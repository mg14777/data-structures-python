class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if not self.value:
            self.value = value
            self.left = None
            self.right = None
            return self

        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        elif value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
        return self

    def contains(self, value):
        # Write your code here.
        if not self.value:
            return False
        if self.value == value:
            return True
        if value < self.value and self.left:
            return self.left.contains(value)
        if value >= self.value and self.right:
            return self.right.contains(value)
        return False
        
    def getMinValue(self):
        # Given a node find the minimum value of its subtree
        if self.left:
            return self.left.getMinValue()
        return self.value
        
    def removeCurNode(self, value, parent=None ):
        noChildren = not self.left and not self.right
        if noChildren and not parent:
            self.value = None
        elif noChildren and parent:
            if parent.left == self:
                parent.left = None
            else:
                parent.right = None
        elif self.right is not None:
            self.value = self.right.value
            self.left = self.right.left
            self.right = self.right.right
        elif self.left is not None:
            self.value = self.left.value
            self.right = self.left.right
            self.left = self.left.left
        else:
            self.value = self.right.getMinValue()
            self.right.remove(self.value, self)
        
    def remove(self, value, parent=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value < self.value and self.left:
            self.left.remove(value, self)
        elif value > self.value and self.right:
            self.right.remove(value, self)
        elif value == self.value:
            self.removeCurNode( self.value, parent )
        return self

    def printInorder(self):
      if self.left:
          self.left.printInorder()
      if self.value:
          print(self.value, end=' ')
      if self.right:
          self.right.printInorder()

    def print(self):
      self.printInorder()
      print()
