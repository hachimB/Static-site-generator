class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This method is not implemented here")
    
    def props_to_html(self):
        result = ""
        if self.props:
            new_list = self.props.items()
            if len(new_list) > 0:
                for item in new_list:
                    result += f' {item[0]}="{item[1]}"'
                return result
        return result
    
    def __repr__(self):
        return f"[ HTMLNode ]:\nTAG: <{self.tag}>\nVALUE: ```{self.value}```\nCHILDREN: {self.children}\nPROPS: {self.props}"
    
