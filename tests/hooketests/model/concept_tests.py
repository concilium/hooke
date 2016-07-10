from nose.plugins.attrib import attr

import Hooke

from ._attributes import concept_attribs
from ._helpers import check_attr, compare_attrs, check_repr

class ConceptTests:

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and attributes of "Concept" model class'''
    
        check_attr( Hooke.model, 'Concept' )
        
        c = Hooke.model.Concept( **concept_attribs )
        compare_attrs( c, concept_attribs )
        check_repr( c, c.id )
    
    @attr( type = 'persistence' )
    def test_persistence( self ):
        '''verify persistence of "Concept" instances'''
        
        ses1 = Hooke.model.SQLiteMemorySession()
        c1 = Hooke.model.Concept( **concept_attribs )
        ses1.add( c1 )
        ses1.commit()
        ses1.close()
    
        ses2 = Hooke.model.SQLiteMemorySession()
        c2 = ses2.query( Hooke.model.Concept ).filter( Hooke.model.Concept.id == concept_attribs['id'] ).one()
        compare_attrs( c2, concept_attribs )
        ses2.delete( c2 )
        ses2.commit()
        ses2.close()
