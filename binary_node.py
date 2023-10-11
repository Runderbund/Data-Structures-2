class BinaryNode:
    def __init__(self):
        self.data = None
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
                
    def search_for_node():
        pass
