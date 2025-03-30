import unittest
from htmlnode import HTMLNode


class TestHtmlnode(unittest.TestCase):
    def test_case1(self):
        tag = "div"
        value = None
        children = [HTMLNode("h1","Welcome!"), HTMLNode("p","This is a text")]
        props = {"id": "parentTag"}
        node1 = HTMLNode(tag, value, children, props)
        self.assertEqual(node1.props_to_html(), ' id="parentTag"')

    def test_case2(self):
        tag = "a"
        value = "Click here!"
        children = None
        props = {"href": "https://www.google.com", "target": "_blank",}
        node = HTMLNode(tag, value, children, props)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_case3(self):
        tag = "a"
        value = "Click here!"
        node = HTMLNode(tag, value)
        self.assertEqual(node.props_to_html(), "")

    def test_case4(self):
        tag = "a"
        value = "Click here!"
        props = {}
        node = HTMLNode(tag, value, props)
        self.assertEqual(node.props_to_html(), "")