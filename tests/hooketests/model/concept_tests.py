from unittest import TestCase
from nose.plugins.attrib import attr

import hooke

from ._attributes import concept_attribs
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
        c1 = hooke.model.Concept( **concept_attribs )
        ses1.add( c1 )
        ses1.commit()
        ses1.close()
    
        ses2 = hooke.model.SQLiteMemorySession()
        c2 = ses2.query( hooke.model.Concept ).filter( hooke.model.Concept.id == concept_attribs['id'] ).one()
        compare_attrs( c2, concept_attribs )
        ses2.delete( c2 )
        ses2.commit()
        ses2.close()
