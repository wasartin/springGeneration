class Table():
    def __init__(self, name, schema, attributes):
        self.name = name
        self.schema = schema
        self.attributes = attributes

    def Name(self):
        return self.name

    def Schema(self):
        return self.schema

    def Attributes(self):
        return self.attributes

    def __str__(self):
        str = ''
        str += f"{self.name}"
        for i in self.attributes:
            str += f"\ti: {self.attributes[i]}"
        return str
