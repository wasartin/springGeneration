class Table():
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

    def Name(self):
        return self.name

    def Attributes(self):
        return self.attributes

    def __str__(self):
        str = ''
        str += f"{self.name}"
        for i in self.attributes:
            str += f"\ti: {self.attributes[i]}"
        return str 
