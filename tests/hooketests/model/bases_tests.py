from nose.plugins.attrib import attr

import Hooke

from ._helpers import check_attr

class HookeModelBase_Tests:
    
    @attr( type = 'existence' )
    def test_for_existence( self ):
#        '''verify existence of "HookeModelBase" class'''
    
        check_attr( Hooke.model, 'HookeModelBase' )
