class Table():
    def __init__(self, name, schema, attributes):
        self._name = name
        self._schema = schema
        self._attributes = attributes

    @property
    def name(self):
        """The name of the table"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def schema(self):
        """The original schema for this table"""
        return self._schema

    @schema.setter
    def schema(self, value):
        self._schema = value

    @schema.deleter
    def schema(self):
        del self._schema

    @property
    def attributes(self):
        """Dictionary of attributes"""
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        self._attributes = value

    @attributes.deleter
    def attributes(self):
        del self._attributes

    def __str__(self):
        str = ''
        str += f"{self.name}"
        for i in self.attributes:
            str += f"\ti: {self.attributes[i]}"
        return str
