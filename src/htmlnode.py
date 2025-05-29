
class HTMLNode:

    def __init__(self,tag = None,value = None,children = None,props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("")

    def props_to_html(self):
        rs = ""
        rsArr = []
        for k,v in self.props.items():
            print(f"{self.props[k]}")
            rsArr.append(f"\"{k}\"=\"{v}\" ")

        for x in rsArr:
            rs += f"{x}"

        rs = rs.strip()
        print(rs)
        return rs

    def __repr__(self):
        return f"tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"
    
    def __eq__(self,target):
        if self.tag == target.tag and self.value == target.value and self.children == target.children and self.props == target.props:
            return True
        else:
            return False
