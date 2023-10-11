from linked_list import LinkedList

class RunMain:
    def __init__(self) -> None:
        self.list = LinkedList()

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

if __name__== '__main__':
    main = RunMain()
    main.append_nodes ()
    main.find_values()