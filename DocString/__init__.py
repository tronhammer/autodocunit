import re

class DocString:
    """Object Representation of a Documentation String"""
    
    is_single = False
    type_defualts = {
        "string": "Hello World!",
        "int": "1",
        "bool": "True",
        "float": "3.14",
        "object": "json_decode('{\"test\":\"test\"}')",
        "array": 'Array()'
    }
    
        
    def factory(self, string):
        return self.__class__( string )

    def test(self, string):
        return string[2:len(self.key)+2] == self.key
        
    def extract_exec(self, haystack):
        var_cmd = re.match(r'^==#{[^}#]*}#', haystack)
        if var_cmd is not None:
            var_exec = var_cmd.group()[4:-2]
            if self.var_type == "object":
                var_exec = "json_decode('{%s}')" % var_exec
            self.var_eq = var_exec
            self.var_desc = haystack[len(var_exec)+6:].strip()
        else:
            self.var_eq = self.type_defualts[ self.var_type ]
            self.var_desc = haystack.strip()

    def __str__(self):
        return "DocString"

class ParamDSI(DocString):
    """Object Representation of a Documentation String"""
    
    is_single = False
    key = "@param"
    
    def __init__(self, string = False):
        if string:
            (var_type, var_name, var_details) = string[len(self.key)+3:].split(" ", 2)
            self.var_type = var_type.strip().lower()
            self.var_name = var_name.strip()
            DocString.extract_exec( self, var_details.strip() )
        
    def __str__(self):
        return "DocString"

class ReturnDSI(DocString):
    """Object Representation of a Documentation String"""
    
    is_single = False
    key = "@return"
    
    def __init__(self, string = False):
        if string:
            (var_type, var_name, var_details) = string[len(self.key)+3:].split(" ", 2)
            self.var_type = var_type.strip().lower()
            self.var_name = var_name.strip()
            DocString.extract_exec( self, var_details.strip() )
        
    def __str__(self):
        return "DocString"
        
class SeeDSI(DocString):
    """Object Representation of a Documentation String"""
    
    is_single = False
    key = "@see"
    
    def __init__(self, string = False):
        if string:
            (self.var_ref) = string[len(self.key)+3:].split(" ", 2)
        
    def __str__(self):
        return "DocString"

class UsesDSI(DocString):
    """Object Representation of a Documentation String"""
    
    is_single = False
    key = "@uses"
    
    def __init__(self, string = False):
        if string:
            (self.var_ref) = string[len(self.key)+3:].split(" ", 2)
        
    def __str__(self):
        return "DocString"
        
# print __name__
# if __name__ == "DocString":
#     from Param import *