import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("T1",TextType.NORMAL,"http://localhost")
        node2 = TextNode("T2",TextType.NORMAL,"http://localhost")
        self.assertNotEqual(node,node2)

    def test_stilleq(self):
        node = TextNode("T1",TextType.LINKS,"http://localhost")
        node2 = TextNode("T1",TextType.LINKS)
        self.assertNotEqual(node,node2)

if __name__ == "__main__":
    unittest.main()
