from enum import Enum

class TextType(Enum):
    NORMAL = "NORMAL"
    ITALIC = "ITALIC"
    CODE = "CODE"
    LINKS = "LINKS"
    IMAGES = "IMAGES"

class TextNode:
    def __init__(self, txt, txt_type, url = None):
        self.text = txt
        self.text_type = txt_type
        self.url = url

    def __eq__(self, target):
        if self.text == target.text and self.text_type == target.text_type and self.url == target.url:
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
