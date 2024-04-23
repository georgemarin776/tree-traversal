import unittest
from tree import Tree
from node import Node

class TestFind(unittest.TestCase):
    def test_find_existing_node(self):
        tree = Tree()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        tree.add(2)
        tree.add(4)
        tree.add(6)
        tree.add(8)

        result = tree.find(4)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, Node)
        self.assertEqual(result.data, 4)

    def test_find_non_existing_node(self):
        tree = Tree()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        tree.add(2)
        tree.add(4)
        tree.add(6)
        tree.add(8)

        result = tree.find(9)
        self.assertEqual(result, None)
