from unittest import TestCase
from nose.plugins.attrib import attr

import hooke

from ._factory import concept_attribs, add_concept, query_concept, delete_concept
from ._helpers import check_attr, compare_attrs, check_repr

class ConceptTests( TestCase ):

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and attributes of "Concept" model class'''
    
        check_attr( hooke.model, 'Concept' )
        
        c = hooke.model.Concept( **concept_attribs )
        compare_attrs( c, concept_attribs )
        check_repr( c, c.id )
    
    @attr( type = 'persistence' )
    def test_persistence( self ):
        '''verify persistence of "Concept" instances'''
        
        ses1 = hooke.model.SQLiteMemorySession()
        add_concept( ses1 )
        ses1.commit()
        ses1.close()
    
        ses2 = hooke.model.SQLiteMemorySession()
        c = query_concept( ses2 )
        compare_attrs( c, concept_attribs )
        delete_concept( ses2 )
        ses2.commit()
        ses2.close()
