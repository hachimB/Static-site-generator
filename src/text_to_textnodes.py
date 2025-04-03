from split_nodes_link import split_nodes_link
from split_nodes_image import split_nodes_image
from textnode import TextNode, TextType
from splitbydelim import split_nodes_delimiter


def text_to_textnodes(text):
    split_bold = split_nodes_delimiter([TextNode(text, TextType.NORMAL_TEXT)], "**", TextType.BOLD_TEXT)
    split_italic = split_nodes_delimiter(split_bold, "_", TextType.ITALIC_TEXT)
    split_code = split_nodes_delimiter(split_italic, "`", TextType.CODE_TEXT)
    split_images = split_nodes_image(split_code)
    nodes = split_nodes_link(split_images)
    return nodes
