class DocBlock:
    """Object Representation of a Documentation Block"""
    id = 0

    def __init__(self, DocStringCollection = []):
        self.DocStringCollection = {}
        for DocStringItem in DocStringCollection:
            register( DocStringItem )

    def register(self, DocStringItem):
        if DocStringItem.key not in self.DocStringCollection:
            self.DocStringCollection[ DocStringItem.key ] = []
        
        self.DocStringCollection[ DocStringItem.key ].append( DocStringItem )
    
    def dissect_defintion(self, definition):
        self.name = definition.split(" ", 1)[1].split("(")[0]
        self.declaration = definition.strip("{}")
        
    def __str__(self):
        return "DocBlock"