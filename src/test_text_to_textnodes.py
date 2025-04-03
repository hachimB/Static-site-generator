import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TextTextToTextnodes(unittest.TestCase):
    def test_several_element(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(new_nodes, [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" with an ", TextType.NORMAL_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word and a ", TextType.NORMAL_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" and an ", TextType.NORMAL_TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL_TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),])
    
    def test_bold_italic(self):
        text = "This is **text** with an _italic_"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(new_nodes,[
                             TextNode("This is ", TextType.NORMAL_TEXT),
                             TextNode("text", TextType.BOLD_TEXT),
                             TextNode(" with an ", TextType.NORMAL_TEXT),
                             TextNode("italic", TextType.ITALIC_TEXT)
                             ])
    
    def test_bold_italic_code(self):
        text = "This is **text** with an _italic_ word and a `code block`"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(new_nodes,[
                             TextNode("This is ", TextType.NORMAL_TEXT),
                             TextNode("text", TextType.BOLD_TEXT),
                             TextNode(" with an ", TextType.NORMAL_TEXT),
                             TextNode("italic", TextType.ITALIC_TEXT),
                             TextNode(" word and a ", TextType.NORMAL_TEXT),
                             TextNode("code block", TextType.CODE_TEXT),
                             ])
    
    def test_images_link(self):
        text = "This is an ![image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(new_nodes,[
                             TextNode("This is an ", TextType.NORMAL_TEXT),
                             TextNode("image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                             TextNode(" and a ", TextType.NORMAL_TEXT),
                             TextNode("link", TextType.LINK, "https://boot.dev")
                             ])
