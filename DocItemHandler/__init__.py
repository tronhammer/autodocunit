import glob
import os
import fnmatch

from DocString import *
from DocBlock import *

class DocItemHandler:
    """Builds DocStrings Out Of A String Set"""
    
    testUnitCollection = {}
    docBlockCollection = {}
    unitDocBlockMap = {}
    functionMap = {}
    unitMap = {}
    
    _tab = "     "
    
    def __init__(self):
        self.DocStringList = [ ParamDSI(), ReturnDSI(), SeeDSI(), UsesDSI() ]
    
    def package_all(self):
        for DBI_name in self.docBlockCollection:
            for DBI in self.docBlockCollection[ DBI_name ]:
                self.package( DBI )
        return self.testUnitCollection
            
    def package(self, DocBlockItem):
        test_unit_name = "_autodocunit_%s" % DocBlockItem.name
        test_unit = "/*\n%s%s\n%s%s\n*/\n" % (self._tab, DocBlockItem.func_synopsis, self._tab, DocBlockItem.func_desc) 
        test_unit += "function %s(){\n" % test_unit_name
        params = []
        param_set = {}
        param_name_matches = {}
        param_indices = []
        for var_param in DocBlockItem.DocStringCollection["@param"]:
            param_set[ var_param.var_name ] = var_param.var_eq
        
        for param_var_name in param_set:
            param_indices.append( DocBlockItem.declaration.index( param_var_name ) )
            param_name_matches[ DocBlockItem.declaration.index( param_var_name ) ] = param_var_name
        
        param_indices.sort()
        
        for param_index in param_indices:
            params.append( param_set[ param_name_matches[ param_index ] ] )
        
        test_unit += "%s$ret = %s(%s);\n" % (self._tab, DocBlockItem.name, ", ".join(params))
        test_unit += "%sreturn $ret == %s;\n" % (self._tab, DocBlockItem.DocStringCollection["@return"][0].var_eq)
        test_unit += "}\n\n"
        
        self.testUnitCollection[ test_unit_name ] = test_unit
        if DocBlockItem.filename not in self.unitMap:
            self.unitMap[ DocBlockItem.filename ] = []
        self.unitMap[ DocBlockItem.filename ].append( test_unit_name )
        self.unitDocBlockMap[ test_unit_name ] = DocBlockItem
    
    def deploy(self):
        if not os.path.exists("./AutoDocUnits"):
            os.makedirs("./AutoDocUnits")
        
        for test_unit_file_path in self.unitMap:
            test_units = self.unitMap[ test_unit_file_path ]
            test_unit_filename = "%s-test-unit.php" % os.path.basename( test_unit_file_path )
            output_content = "<?php\n"
            call_list = []
            include_list = []
            function_list = []
            
            for test_unit_name in test_units:
                unit_doc_block = self.unitDocBlockMap[ test_unit_name ]
                include_files = self.functionMap[ unit_doc_block.name ]
                for include_file in include_files:
                    include_list.append( "include_once('%s');" % test_unit_file_path )
                function_list.append( "%s" % self.testUnitCollection[ test_unit_name ] )
                call_list.append( "\"%s\" => %s()" % (test_unit_name,test_unit_name) )
            
            output_content += "%s\n\n%s\necho json_encode(array(%s));\n" % ( "\n".join( list(set(include_list)) ), "\n".join( function_list ), ",".join( call_list ) )
            
            outfile = open( "./AutoDocUnits/%s" % test_unit_filename, "w" )
            outfile.write( output_content )
            outfile.close()
        
    def dissect(self, root, filename):
        CurrentDocBlock = 0 # DocBlock In Rotation
        file_fullpath = os.path.abspath( os.path.join(root, filename) )
        collector_on = 0
        i = 0
        
        with open(file_fullpath) as f:
            content = f.readlines()
            for ln in content:
                clean_ln = ln.strip()
                if clean_ln == "/**":
                    CurrentDocBlock = DocBlock()
                    CurrentDocBlock.id = i
                    collector_on = 1
                    i = i +1
                elif clean_ln[-2:] == "*/":
                    collector_on = -1
                elif str(CurrentDocBlock) == "DocBlock":
                    if collector_on == -1 and clean_ln[:8] == "function":
                        if str(CurrentDocBlock) == "DocBlock" and len(CurrentDocBlock.DocStringCollection):
                            CurrentDocBlock.dissect_defintion( clean_ln )
                            CurrentDocBlock.func_desc = CurrentDocBlock.func_desc.strip()
                            CurrentDocBlock.filename = file_fullpath
                            if CurrentDocBlock.name not in self.functionMap:
                                self.functionMap[ CurrentDocBlock.name ] = []
                            self.functionMap[ CurrentDocBlock.name ].append( file_fullpath )
                            if file_fullpath not in self.docBlockCollection:
                                self.docBlockCollection[ file_fullpath ] = []
                            self.docBlockCollection[ file_fullpath ].append( CurrentDocBlock )
                        CurrentDocBlock = 0
                        collector_on = 0
                    elif len(clean_ln) > 0 and clean_ln[0] == "*":
                        # Change this to use SynopsisDSI, DescriptionDSI and NameDSI instead
                        # Use .test() functions to see which the first line is
                        #   Be flexible enough not to require each but still acquire them if they exist
                        if collector_on == 1:
                            CurrentDocBlock.func_synopsis = clean_ln[2:].strip()
                            CurrentDocBlock.func_desc = ""
                            collector_on += 1
                        elif clean_ln == '*':
                            collector_on += 1
                        elif collector_on == 3:
                            CurrentDocBlock.func_desc += " %s" % clean_ln[2:].strip()
                        else:
                            for DS in self.DocStringList:
                                if DS.test( clean_ln ):
                                    CurrentDocBlock.register( DS.factory( clean_ln ) )

    def __str__(self):
        return "DocItemHandler"
