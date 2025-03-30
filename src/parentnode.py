from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        result = ""
        if self.tag == None:
            raise ValueError("The parent node should contain tags")
        
        if len(self.children) == 0:
            raise ValueError("A child should have a value")
        
        for elem in self.children:
            result += elem.to_html()
        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"
        