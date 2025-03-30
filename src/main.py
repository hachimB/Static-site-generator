from textnode import TextType
from textnode import TextNode
from htmlnode import HTMLNode


def main():
    t_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(t_node)
    print()

    html_node1 = HTMLNode("a", "Click here!", None, {"href": "https://www.google.com", "target": "_blank",})
    print(html_node1)
    print()

    html_node2 = HTMLNode("div", None, [HTMLNode("h1","Welcome!"), HTMLNode("p","This is a text")], {"id": "parentTag"})
    print(html_node2)
    print()

main()
