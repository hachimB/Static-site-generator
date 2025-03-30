from leafnode import LeafNode
import unittest


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click here!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click here!</a>')

    def test_leaf_to_html_withoutag(self):
        node = LeafNode(None, "Good morning!")
        self.assertEqual(node.to_html(), "Good morning!")

    def test_leaf_to_html_valuerror(self):
        node = LeafNode("a", None)
        with self.assertRaises(ValueError):
            node.to_html()