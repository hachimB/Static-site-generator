from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph",
    HEADING = "heading",
    CODE = "code",
    QUOTE = "quote",
    UNORDERED_LIST = "unordered_list",
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    headings = ['# ','## ','### ','#### ','##### ','###### ']
    for heading in headings:
        if markdown.startswith(heading):
            return BlockType.HEADING
    
    if markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
    
    lines = markdown.split("\n")
    
    if all(line.lstrip().startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.lstrip().startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    i = 1
    f = True
    for line in lines:
        if line.lstrip().startswith(f"{i}. "):
            i += 1
            continue
        else:
            f = False
    if f == True:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
    