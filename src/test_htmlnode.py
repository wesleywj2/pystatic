import unittest
from htmlnode import HTMLNode 

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        props = {"href":"http://mydomain.com","target":"_blank"}
        node = HTMLNode("p", "some paragraph",None,props)
        node2 = HTMLNode("p", "some paragraph",None,props)
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        props = {"href":"http://mydomain.com","target":"_blank"}
        node = HTMLNode("p", "some paragraph",None,props)
        node2 = HTMLNode("a", "some paragraph",None,props)
        self.assertNotEqual(node, node2)

    def test_eq_tag_and_value_only(self):
        # props = {"href":"http://mydomain.com","target":"_blank"}
        node = HTMLNode("a", "some paragraph")
        node2 = HTMLNode("a", "some paragraph")
        self.assertEqual(node, node2)