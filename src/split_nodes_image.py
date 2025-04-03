from textnode import TextNode, TextType
from extract_markdown_images import extract_markdown_images

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        # If the node is normal text, no splitting is needed
        if node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        if not text:
            continue

        # Extract all images from the text
        images = extract_markdown_images(text)

        # If no images are found, keep the original node
        if not images:
            new_nodes.append(node)
            continue

        # Iteratively process the text for each image
        for image_alt, image_link in images:
            image_markdown = f"![{image_alt}]({image_link})"
            
            # Split the text into two parts: before and after the current image
            parts = text.split(image_markdown, 1)

            # Add the text before the image, if it exists
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.NORMAL_TEXT))

            # Add the image node
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

            # Update text to the remaining part after the current image
            text = parts[1] if len(parts) > 1 else ""

        # If there's leftover text after processing all images, add it
        if text:
            new_nodes.append(TextNode(text, TextType.NORMAL_TEXT))

    return new_nodes