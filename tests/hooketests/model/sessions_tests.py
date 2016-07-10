from nose.plugins.attrib import attr

import Hooke

from ._helpers import check_attr

class SQLiteMemorySessionTests:

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence of "SQLiteMemorySession" class'''
    
        check_attr( Hooke.model, 'SQLiteMemorySession' )
