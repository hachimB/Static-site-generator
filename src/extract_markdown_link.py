import re
def extract_markdown_link(text):
    result = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return result
