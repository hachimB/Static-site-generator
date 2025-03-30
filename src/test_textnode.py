import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node = TextNode("Thanks", TextType.NORMAL_TEXT, "https://www.boot.dev")
        node2 = TextNode("Thanks", TextType.NORMAL_TEXT, "https://www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("Hello", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("Hello", TextType.IMAGE, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("welcome to bootdev", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("welcome here!", TextType.IMAGE, None)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()