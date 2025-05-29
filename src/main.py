from textnode import TextNode,TextType
from htmlnode import HTMLNode

def main():
    obj = TextNode("DummyText",TextType.NORMAL,"http://mydomain.com")
    print(obj)
    x = {"href":"https://google.com","target": "_blank"}

    a = HTMLNode("p","text of paragraph",None,x)
    a.props_to_html() 

main()

