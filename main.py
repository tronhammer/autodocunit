#!/usr/bin/python
"""
    Auto Test Unit Generation From Inline Documentation Module
    
    This will create test units from properly formatted inline
    documentation in code/program files.

    @package AutoDocUnit
    @category Main
    @version 0.1.2b
    @since 0.1.1b
    @author Sean Murray <smurraysb@gmail.com>
    @copyright Tronnet
    @license GPLv2

        This program is free software; you can redistribute it and/or modify
        it under the terms of the GNU General Public License, version 2, as 
        published by the Free Software Foundation.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program; if not, write to the Free Software
        Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

import glob
import os
import fnmatch

from DocItemHandler import *

if __name__ == "__main__":
    DIB = DocItemHandler()

    for root, dirnames, filenames in os.walk('./'):
        for filename in fnmatch.filter(filenames, '*.php'):
            DIB.dissect( root, filename )
            
    DIB.package_all()
    # 
    # print DIB.testUnitCollection
    # print "============########============"
    # print DIB.docBlockCollection
    # print "============########============"
    # print DIB.functionMap
    # print "============########============"
    # print DIB.unitMap
    # print "============########============"
    # print DIB.unitDocBlockMap
    # 
    
    DIB.deploy()
    
    