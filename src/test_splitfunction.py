from splitbydelim import split_nodes_delimiter
import unittest
from textnode import TextNode, TextType

class TestSplitFunction(unittest.TestCase):
    def test_code_block(self):
        node = [TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT)]

        self.assertEqual(split_nodes_delimiter(node, "`", TextType.CODE_TEXT), [
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" word", TextType.NORMAL_TEXT)
        ])
    
    def test_bold(self):
        node2 = [TextNode("This is text with a **bold** word", TextType.NORMAL_TEXT)]

        self.assertEqual(split_nodes_delimiter(node2, "**", TextType.BOLD_TEXT), [
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" word", TextType.NORMAL_TEXT)
        ])
    
    def test_wrong_type(self):
        node3 = [TextNode("This is text with a **bold** word", TextType.BOLD_TEXT)]

        self.assertEqual(split_nodes_delimiter(node3, "**", TextType.BOLD_TEXT), [
            TextNode("This is text with a **bold** word", TextType.BOLD_TEXT)
        ])
    
    def test_without_delimiter(self):
        node4 = [TextNode("This text do not delimiter", TextType.NORMAL_TEXT)]

        self.assertEqual(split_nodes_delimiter(node4, "_", TextType.ITALIC_TEXT), [
            TextNode("This text do not delimiter", TextType.NORMAL_TEXT)
        ])
    
    def test_several_delimiters(self):
        node = [TextNode("This is text with a first `code block` and another `code block`", TextType.NORMAL_TEXT)]

        self.assertEqual(split_nodes_delimiter(node, "`", TextType.CODE_TEXT), [
            TextNode("This is text with a first ", TextType.NORMAL_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" and another ", TextType.NORMAL_TEXT),
            TextNode("code block", TextType.CODE_TEXT)
        ])
    
