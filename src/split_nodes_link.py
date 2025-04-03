from textnode import TextNode, TextType
from extract_markdown_link import extract_markdown_link

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        # If the node is normal text, no splitting is needed
        if node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        if not text:
            continue

        # Extract all links from the text
        links = extract_markdown_link(text)

        # If no links are found, keep the original node
        if not links:
            new_nodes.append(node)
            continue

        # Iteratively process the text for each link
        for alt_link, url_link in links:
            link_markdown = f"[{alt_link}]({url_link})"
            
            # Split the text into two parts: before and after the current link
            parts = text.split(link_markdown, 1)

            # Add the text before the link, if it exists
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.NORMAL_TEXT))

            # Add the link node
            new_nodes.append(TextNode(alt_link, TextType.LINK, url_link))

            # Update text to the remaining part after the current link
            text = parts[1] if len(parts) > 1 else ""

        # If there's leftover text after processing all links, add it
        if text:
            new_nodes.append(TextNode(text, TextType.NORMAL_TEXT))

    return new_nodes