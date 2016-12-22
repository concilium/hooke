from unittest import TestCase
from nose.plugins.attrib import attr

import hooke

from ._factory import history_attribs, add_history, query_history, delete_history, query_concept, query_palette, query_concept_palette
from ._helpers import check_attr, compare_attrs, check_repr, SQLiteMemorySession

class HistoryTests( TestCase ):

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and attributes of "History" model class'''
    
        check_attr( hooke.model, 'History' )
        
        h = hooke.model.History( **history_attribs )
        compare_attrs( h, history_attribs )
        check_repr( h, h.id )
    
    @attr( type = 'persistence' )
    def test_persistence( self ):
        '''verify persistence of "History" instances'''

        ses1 = SQLiteMemorySession()
        add_history( ses1 )
        ses1.commit()
        ses1.close()
    
        ses2 = SQLiteMemorySession()
        h = query_history( ses2 )
        compare_attrs( h, history_attribs )
        delete_history( ses2 )
        ses2.commit()
        ses2.close()

    @attr( type = 'association' )
    def test_associations( self ):
        '''verify behavior of history associations'''
        
        ses = SQLiteMemorySession()
        add_history( ses )
        ses.commit()

        h = query_history( ses )
        c = query_concept( ses )
        p = query_palette( ses )
        cp = query_concept_palette( ses )
        
        assert h.concept_palette == cp
        assert h.concept == c
        assert h.palette == p
        
        delete_history( ses )
        ses.commit()
        ses.close()