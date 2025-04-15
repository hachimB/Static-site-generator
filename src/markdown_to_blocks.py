def markdown_to_blocks(markdown):
    new_list = []
    splitted_text = markdown.split("\n\n")
    for block in splitted_text:
        if not block:
            continue
        splitted_block = block.strip().split("\n")
        for i in range(len(splitted_block)):
            # Strip whitespace from each line and normalize internal spaces
            line = splitted_block[i].strip()
            # Replace multiple spaces with a single space
            while "  " in line:
                line = line.replace("  ", " ")
            splitted_block[i] = line
        new_list.append("\n".join(splitted_block))
        
    return new_list