from textnode import TextNode
from textnode import TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(old_node)
            continue
        
        text = old_node.text
        if delimiter not in text:
            new_nodes.append(old_node)
            continue
            
        # Find the opening delimiter
        start_idx = text.find(delimiter)
        # Find the closing delimiter after the opening one
        end_idx = text.find(delimiter, start_idx + len(delimiter))

        
        if end_idx == -1:
            raise Exception(f"No closing delimiter found for {delimiter}")
            
        # Split the text into three parts
        before_text = text[:start_idx]
        between_text = text[start_idx + len(delimiter):end_idx]
        after_text = text[end_idx + len(delimiter):]
        
        # Create nodes for each part
        if before_text:
            new_nodes.append(TextNode(before_text, TextType.NORMAL_TEXT))
        if between_text:
            new_nodes.append(TextNode(between_text, text_type))
        if after_text:
            # Create a new node with the after_text and recursively process it
            after_nodes = split_nodes_delimiter([TextNode(after_text, TextType.NORMAL_TEXT)], delimiter, text_type)
            new_nodes.extend(after_nodes)

        
    return new_nodes