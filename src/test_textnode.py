import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq_pass(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_eq_pass2(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)    

    def test_eq_false(self):
        node = TextNode("This is a text node 1", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node 2", "bold", "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("Test Node", "bold", "https://www.boot.dev")
        node2 = TextNode("Test Node", "italic", "https://www.boot.dev")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
