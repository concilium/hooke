from unittest import TestCase
from nose.plugins.attrib import attr

import hooke

from ._helpers import check_attr

class SQLiteMemorySessionTests( TestCase ):

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence of "SQLiteMemorySession" class'''
    
        check_attr( hooke.model, 'SQLiteMemorySession' )
