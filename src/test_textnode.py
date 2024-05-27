import unittest

from textnode import TextNode, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_text_node_to_html_node(self):
        node = text_node_to_html_node(TextNode("I am a text", "text"))
        node2 = LeafNode(None, "I am a text")
        self.assertEqual(node, node2)

    def test_bold_text_node_to_bold_html_node(self):
        node = text_node_to_html_node(TextNode("I am a bold text", "bold"))
        node2 = LeafNode("b", "I am a bold text")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
