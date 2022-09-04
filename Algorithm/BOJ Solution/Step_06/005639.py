import sys

class Node:

    def __init__(self, value, up = None, down = None):
        self.value = value
        self.up = up
        self.down = down

    def up_node(self):
        return self.up

    def down_node(self):
        return self.down

    def get_value(self):
        return self.value


class BinarySearchTree:

    def __init__(self, root):
        self.root = Node(root)
        self.min_number = root

    def tree_root(self):
        return self.root

    def add_node(self, node):
        now_cursor = self.root
        while True:
            last_node = now_cursor
            if node.value > now_cursor.value:
                now_cursor = now_cursor.up_node()
                if now_cursor is None:
                    now_cursor = node
                    now_cursor.down = last_node
                    last_node.up = now_cursor
                    break
            elif node.value < now_cursor.value:
                now_cursor = now_cursor.down_node()
                if now_cursor is None:
                    now_cursor = node
                    now_cursor.up = last_node
                    last_node.down = now_cursor
                    break
    
    def postorder(self, node:Node):
        if node.up_node() is not None:
            self.postorder(self, node.up_node())
        if node.up_node() is not None:
            self.postorder(self, node.down_node())
        print(node.get_value())

tree = BinarySearchTree(int(sys.stdin.readline()))

for input_number in sys.stdin:
    this_node = Node(int(input_number))
    tree.add_node(this_node)

tree.postorder(tree.tree_root())