class BinaryNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, data):
        if data < self.data:
            if self.left is None:
                self.left = BinaryNode(data)
            else:
                self.left.insert_node(data)
        else:
            if self.right is None:
                self.right = BinaryNode(data)
            else:
                self.right.insert_node(data)

    def search_for_node(self, data):
        if self.data == data:
            return self
        elif data < self.data and self.left is not None:
            return self.left.search_for_node(data)
        elif data > self.data and self.right is not None:
            return self.right.search_for_node(data)
        return None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_node(self, data):
        if self.root is None:
            self.root = BinaryNode(data)
        else:
            self.root.insert_node(data)

    def search_for_node(self, data):
        if self.root is None:
            return None
        else:
            return self.root.search_for_node(data)
