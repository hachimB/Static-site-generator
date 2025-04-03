import re
def extract_markdown_images(text):
    result = re.findall(r"\!\[(.*?)\]\((.*?)\)",text)
    return result