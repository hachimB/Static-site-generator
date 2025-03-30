from parentnode import ParentNode
from leafnode import LeafNode
import unittest

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",)
    
    def test_to_html_with_grand_children2(self):
        grandchild = LeafNode("i", "Hello")
        child = ParentNode("p", [grandchild])
        parent = ParentNode("section", [child])
        self.assertEqual(parent.to_html(), "<section><p><i>Hello</i></p></section>")
    
    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_with_no_tag(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_with_no_children_and_no_tag(self):
        parent_node = ParentNode(None, [])
        with self.assertRaises(ValueError):
            parent_node.to_html()