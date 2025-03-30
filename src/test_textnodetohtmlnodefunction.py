from textnode import TextNode, TextType, text_node_to_html_node
import unittest


class TestTextNodeToHTMLNodeFunction(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
    
    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, {"href": "https://google.com"})

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "/home/username/pictures")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "/home/username/pictures", "alt": "This is an image"})
    
    def test_node_equal_none(self):
        with self.assertRaises(TypeError):
            text_node_to_html_node(None)
    
    def test_text_type_error(self):
        node = TextNode("This is a text node", None)
        with self.assertRaises(TypeError):
            text_node_to_html_node(node)