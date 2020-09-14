class Table:
    def __init__(self, name='', schema='', attributes=''):
        self._name = name
        self._schema = schema
        self._attributes = attributes

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_schema(self):
        return self._schema

    def set_schema(self, value):
        self._schema = value

    def get_attributes(self):
        return self._attributes

    def set_attributes(self, value):
        self._attributes = value

    def get_str(self):
        str = ''
        str += f"{self._name}\n"
        for key, value in self._attributes.items():
            str += f"\t{key}: {value}\n"
        return str
