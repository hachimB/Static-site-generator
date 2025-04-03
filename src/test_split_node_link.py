import unittest
from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://google.com) and another [second link](https://www.boot.dev)", 
            TextType.NORMAL_TEXT,)
        new_nodes = split_nodes_link([node])
        
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL_TEXT),
                TextNode("link", TextType.LINK, "https://google.com"),
                TextNode(" and another ", TextType.NORMAL_TEXT),
                TextNode("second link", TextType.LINK, "https://www.boot.dev"),
                ], new_nodes,)
    
    def test_split_link(self):
        node = TextNode(
            "This is text with a [link](https://google.com)", 
            TextType.NORMAL_TEXT,)
        new_nodes = split_nodes_link([node])
        
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL_TEXT),
                TextNode("link", TextType.LINK, "https://google.com")], 
                new_nodes,)

    def test_split_with_text_type_not_TEXT(self):
        node = TextNode(
            "This is text with a [link](https://google.com) and another [second link](https://www.boot.dev)", 
            TextType.LINK,)
        new_nodes = split_nodes_link([node])

        self.assertListEqual([TextNode(
            "This is text with a [link](https://google.com) and another [second link](https://www.boot.dev)", 
            TextType.LINK,)], new_nodes)
    
    def test_split_with_no_text(self):
        node = TextNode(
            "", 
            TextType.NORMAL_TEXT,)
        new_nodes = split_nodes_link([node])

        self.assertListEqual([], new_nodes)
    
    def test_split_with_no_url_link(self):
        node = TextNode(
            "This is a normal text", 
            TextType.NORMAL_TEXT,)
        new_nodes = split_nodes_link([node])

        self.assertListEqual([TextNode("This is a normal text", TextType.NORMAL_TEXT)], new_nodes)
    
