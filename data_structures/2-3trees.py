#!/usr/bin/python
class Node:
    def __init__(self, data, par = None):
        #print ("Node __init__: " + str(data))
        self.data = list([data])
        self.parent = par
        self.child = list()

    def __str__(self):
        if self.parent:
            return str(self.parent.data) + ' : ' + str(self.data)
        return 'Root: ' + str(self.data)

    def __lt__(self, node):
        return self.data[0] < node.data[0]

    def _isLeaf(self):
        return len(self.child) == 0

    def _add(self, new_node):
        #Print ("node _add: "str(new_node.data) + ' to ' +str(self.data))
        for child in new_node.child:
            child.parent = self
        self.data.extend(new_node.data)
        self.data.sort()
        self.child.extend(new_node.child)
        if len(self.child) > 1:
            self.child.sort()
        if len(self.data) > 2:
            self._split()

    def _insert(self, new_node):
        if self._isLeaf():
            self._add(new_node)
        elif new_node.data[0] > self.data[-1]:
            self.child[-1]._insert(new_node)
        else:
            for i in range(0, len(self.data)):
                if new_node.data[0] < self.data[i]:
                    self.child[i]._insert(new_node)
                    break

    def _split(self):
        left_child = Node(self.data[0], self)
        right_child = Node(self.data[2], self)
        if self.child:
            self.child[0].parent = left_child
            self.child[1].parent = left_child
            self.child[2].parent = right_child
            self.child[3].parent = right_child
            left_child.child = [self.child[0], self.child[1]]
            right_child.child = [self.child[2], self.child[3]]

        self.child = [left_child]
        self.child.append(right_child)
        self.data = [self.data[1]]

        if self.parent:
            if self in self.parent.child:
                self.parent.child.remove(self)
            self.parent._add(self)
        else:
            left_child.parent = self
            right_child.parent = self

    def _find(self, item):
        if item in self.data:
            return item
        elif self._isLeaf():
            return False
        elif item > self.data[-1]:
            return self.child[-1]._find(item)
        else:
            for i in range(len(self.data)):
                if item < self.data[i]:
                    return self.child[i]._find(item)

    def _remove(self, item):
        pass

    def _preorder(self):
        print(self)
        for child in self.child:
            child._preorder()


class Tree:
    def __init__(self):
        print("Tree __init__")
        self.root = None

    def insert(self, item):
        print("Tree insert: "+ str(item))
        if self.root is None:
            self.root = Node(item)
        else:
            self.root._insert(Node(item))
            while self.root.parent:
                self.root = self.root.parent
        return True

    def remove(self, item):
        self.root.remove(self, item)

    def printTop2Tiers(self):
        print('--top 2 Tiers--')
        print(str(self.root.data))
        for child in self.root.child:
            print (str(child.data), end='')
            print(' ')

    def find(self, item):
        return self.root._find(item)

    def preorder(self):
        #traverses tree
        print('--preorder---')
        self.root._preorder()



tree = Tree()
lst = [13, 7, 24, 15, 4, 29, 20, 16, 19, 1, 5, 22, 17]
for item in lst:
    tree.insert(item)
tree.printTop2Tiers()
print("Search for 17")
print(tree.find(17))
