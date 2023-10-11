from linked_list import LinkedList
from binary_node import BinarySearchTree

class RunMain:
    def __init__(self) -> None:
        self.list = LinkedList()
        self.tree = BinarySearchTree()

    def append_nodes(self):
        print("\nAdd a new node with the value of 5")
        self.list.append_node(5)
        print("\nAdd a new node with the value of 10")
        self.list.append_node(10)
        print("\nAdd a new node with the value of 55")
        self.list.append_node(55)

    def find_values(self):
        print("\nSearch for a node with value of 10")
        print(self.list.find_node(10))
        print("\nSearch for a node with the value of 22")
        print(self.list.find_node(22))


    def populate_tree(self):
        print("\nInserting nodes into the binary tree")
        self.tree.insert_node(50)
        self.tree.insert_node(30)
        self.tree.insert_node(70)
        self.tree.insert_node(15)
        self.tree.insert_node(75)

    def search_tree(self):
        print("\nSearching for a node with value 70 in the binary tree")
        result = self.tree.search_for_node(70)
        print(f"Node found: {result.data if result else None}")

        print("\nSearching for a node with value 100 in the binary tree")
        result = self.tree.search_for_node(100)
        print(f"Node found: {result.data if result else None}")


    def traverse_tree_in_order(self):
        print("\nPerforming in-order tree traversal:")
        result = self.tree.in_order_traversal()
        print("In-order traversal:", result)

if __name__ == '__main__':
    main = RunMain()
    main.append_nodes()
    main.find_values()
    main.populate_tree()
    main.search_tree()
    main.traverse_tree_in_order()
