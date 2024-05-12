import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node1 = HTMLNode("div", "Hello, world!", None, {"class": "greeting", "href": "https://boot.dev"})
        node2 = HTMLNode("div", "Hello, world!", None, {"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(node1, node2)
    
    def test_to_html_props_false(self):
        node1 = HTMLNode(None, "Hello, world!", None, {"class": "greeting", "href": "https://boot.dev"})
        node2 = HTMLNode(None, "Hello, world!", None, {"class": "greeting", "href": "https://boot.devphish"})
        self.assertEqual(node1, node2)
    
    def test_props_to_html(self):
        node1 = HTMLNode("div", "Hello, world!", None, {"class": "greeting", "href": "https://boot.dev"})
        node1_html_props = node1.props_to_html()
        node1_html_props_test_case = " class=\"greeting\" href=\"https://boot.dev\""
        self.assertEqual(node1_html_props, node1_html_props_test_case)

    def test_leaf_node_eq_pass(self):
        node1 = LeafNode("p", "This is a paragraph", {"href": "https://www.google.com"})
        node2 = LeafNode("p", "This is a paragraph", {"href": "https://www.google.com"})
        self.assertEqual(node1, node2)

    def test_leaf_node_eq_fail(self):
        node1 = LeafNode("p", "This is a paragraph", {"href": "https://www.google.com"})
        node2 = LeafNode("p", "This is a paragraph but different", {"href": "https://www.google.com"})
        self.assertEqual(node1, node2)

    def test_leaf_node_to_html_pass(self):
        node1_html = LeafNode("p", "This is a paragraph", {"href": "https://www.google.com"}).to_html()
        node1_html_test = "<p href=\"https://www.google.com\">This is a paragraph</p>"
        self.assertEqual(node1_html, node1_html_test)

    def test_leaf_node_to_html_pass_2(self):
        node1_html = LeafNode(None, "This is a paragraph", None).to_html()
        node1_html_test = "This is a paragraph"
        self.assertEqual(node1_html, node1_html_test)