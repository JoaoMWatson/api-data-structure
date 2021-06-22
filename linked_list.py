class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str({node.data})} ->'
            node = node.next_node

        ll_string += " None"
        print(ll_string)
        print(f'last {self.last_node.data}')
        print(f'head {self.head.data}')

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
            return

        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_and(self, data):
        if self.head is None:
            self.insert_beginning(data)
            return

        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

ll = LinkedList()
ll.insert_beginning('data1')
ll.insert_beginning('data2')
ll.insert_at_and('end')
ll.print_ll()