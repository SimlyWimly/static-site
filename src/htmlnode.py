class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html function Not implemented yet")

    def props_to_html(self):
        if self.props == None:
            return ""
        html_props = ""
        for prop in self.props:
            html_props += f" {prop}=\"{self.props[prop]}\""
        return html_props

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf Nodes require a value")
        if self.tag != None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        if self.tag == None:
            return self.value

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        html_node = ""
        if self.tag == None:
            raise ValueError("Parent Nodes require a tag")
        if self.children == None:
            raise ValueError("Parent Nodes require a child")
        for children in self.children:
            html_node += children.to_html()
        return f"<{self.tag}{self.props_to_html()}>" + html_node + f"</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
        