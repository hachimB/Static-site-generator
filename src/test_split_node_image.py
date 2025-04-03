import unittest
from split_nodes_image import split_nodes_image
from textnode import TextNode, TextType

class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", 
            TextType.NORMAL_TEXT,)
        new_nodes = split_nodes_image([node])
        
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL_TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL_TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                ],new_nodes,)
    
    def test_split_image(self):
        node = TextNode(
            "This is text with one image link ![image](https://i.imgur.com/zjjcJKZ.png)", 
            TextType.NORMAL_TEXT,)
        new_nodes = split_nodes_image([node])
        
        self.assertListEqual(
            [
                TextNode("This is text with one image link ", TextType.NORMAL_TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")], 
                new_nodes,)

    def test_split_with_text_type_not_TEXT(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", 
            TextType.IMAGE,)
        new_nodes = split_nodes_image([node])

        self.assertListEqual([TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", 
            TextType.IMAGE,)], new_nodes)
    
    def test_split_with_no_text(self):
        node = TextNode(
            "", 
            TextType.NORMAL_TEXT,)
        new_nodes = split_nodes_image([node])

        self.assertListEqual([], new_nodes)
    
    def test_split_with_no_image_link(self):
        node = TextNode(
            "This is a normal text", 
            TextType.NORMAL_TEXT,)
        new_nodes = split_nodes_image([node])

        self.assertListEqual([TextNode("This is a normal text", TextType.NORMAL_TEXT)], new_nodes)
    
