from enum import Enum
from leafnode import LeafNode
class TextType(Enum):
    NORMAL_TEXT = "normal"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"


def text_node_to_html_node(text_node):
    if not text_node:
        raise TypeError("You should use a text node!")
    
    match(text_node.text_type):
        case TextType.NORMAL_TEXT:
            return LeafNode(None, text_node.text)

        case TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text)
        
        case TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text)
        
        case TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})

        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        
        case _:
            raise TypeError("text type error!")
        
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            texts_equal = self.text == other.text
            texts_type_equal = self.text_type == other.text_type
            urls_equal = self.url == other.url
            return texts_equal and texts_type_equal and urls_equal
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    