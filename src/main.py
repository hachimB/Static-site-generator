from textnode import TextType
from textnode import TextNode


def main():
    t_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(t_node)

main()
