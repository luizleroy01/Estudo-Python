class Node:
    def __init__(self, leaf=True):
        self.keys = []
        self.values = []
        self.leaf = leaf
        self.next = None
    
    def add_key_value(self, key, value):
        self.keys.append(key)
        self.values.append(value)
        
    def split(self, order):
        mid = len(self.keys) // 2
        new_node = Node(leaf=self.leaf)
        new_node.keys = self.keys[mid:]
        new_node.values = self.values[mid:]
        self.keys = self.keys[:mid]
        self.values = self.values[:mid]
        return new_node


class BPlusTree:
    def __init__(self, order):
        self.root = Node(leaf=True)
        self.order = order
    
    def insert(self, key, value):
        if key in self.root.keys:
            index = self.root.keys.index(key)
            self.root.values[index] = value
            return
        
        if len(self.root.keys) == self.order:
            new_root = Node(leaf=False)
            new_root.children.append(self.root)
            new_node = self.root.split(self.order)
            new_root.keys.append(new_node.keys[0])
            new_root.children.append(new_node)
            self.root = new_root
        
        self.insert_non_full(self.root, key, value)
    
    def insert_non_full(self, node, key, value):
        if node.leaf:
            index = 0
            for i in range(len(node.keys)):
                if key > node.keys[i]:
                    index = i + 1
            node.keys.insert(index, key)
            node.values.insert(index, value)
        else:
            index = 0
            for i in range(len(node.keys)):
                if key > node.keys[i]:
                    index = i + 1
            if len(node.children[index].keys) == self.order:
                new_node = node.children[index].split(self.order)
                node.keys.insert(index, new_node.keys[0])
                node.children.insert(index + 1, new_node)
                if key > node.keys[index]:
                    index += 1
            self.insert_non_full(node.children[index], key, value)
    
    def search(self, key):
        return self.search_node(self.root, key)
    
    def search_node(self, node, key):
        if node.leaf:
            index = node.keys.index(key) if key in node.keys else -1
            if index != -1:
                return node.values[index]
            else:
                return None
        else:
            index = 0
            for i in range(len(node.keys)):
                if key > node.keys[i]:
                    index = i + 1
            return self.search_node(node.children[index], key)


# Example usage:
if __name__ == "__main__":
    bptree = BPlusTree(order=3)
    bptree.insert(1, "One")
    bptree.insert(2, "Two")
    bptree.insert(3, "Three")
    bptree.insert(4, "Four")
    bptree.insert(5, "Five")

    print(bptree.search(3))  # Output: Three
    print(bptree.search(6))  # Output: None
