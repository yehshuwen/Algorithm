#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: SHU-WEN YEH

# Perform Zig-Zag rotation on a Splay Tree

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def splay(self, root, key):
        if not root or root.key == key:
            return root
	
	# WRITE YOUR CODE HERE

        # Key lies in the left subtree
        if key < root.key:
            # If key is not in tree, recur on the left child
            if not root.left:
                return root

            # Zig-Zag (Left Right)
            if key > root.left.key:
                root.left = self.left_rotate(root.left)

            if root.left:
                return self.right_rotate(root)
            else:
                return root
            
        # Key lies in the right subtree

        else:
            if not root.right:
                return root
            
            return root

    def search(self, key):
        self.root = self.splay(self.root, key)
        return self.root and self.root.key == key

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)


# Example Usage
tree = SplayTree()

# Example manual tree setup
tree.root = Node(30)
tree.root.left = Node(20)
tree.root.right = Node(40)
tree.root.left.left = Node(10)
tree.root.left.right = Node(25)

print("\nSearching for 25...")
found = tree.search(25)
print("Found:", found)
print("Preorder after search:")
tree.preorder(tree.root)
