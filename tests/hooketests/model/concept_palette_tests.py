from unittest import TestCase
from nose.plugins.attrib import attr

import hooke

from ._factory import concept_palette_attribs, add_concept_palette, query_concept_palette, delete_concept_palette, query_concept, query_palette
from ._helpers import check_attr, compare_attrs, check_assoc_repr

class ConceptPaletteTests( TestCase ):

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and attributes of "ConceptPalette" model class'''
    
        check_attr( hooke.model, 'ConceptPalette' )
        
        cp = hooke.model.ConceptPalette( **concept_palette_attribs )
        compare_attrs( cp, concept_palette_attribs )
        check_assoc_repr( cp, cp.concept_id, cp.palette_id )
    
    @attr( type = 'persistence' )
    def test_persistence( self ):
        '''verify persistence of "ConceptPalette" instances'''
        
        ses1 = hooke.model.SQLiteMemorySession()
        add_concept_palette( ses1 )
        ses1.commit()
        ses1.close()
    
        ses2 = hooke.model.SQLiteMemorySession()
        cp = query_concept_palette( ses2 )
        compare_attrs( cp, concept_palette_attribs )
        delete_concept_palette( ses2 )
        ses2.commit()
        ses2.close()
    
    @attr( type = 'association' )
    def test_associations( self ):
        '''verify behavior of concept-to-palette association'''
        
        ses = hooke.model.SQLiteMemorySession()
        add_concept_palette( ses )
        ses.commit()

        c = query_concept( ses )
        p = query_palette( ses )
        cp = query_concept_palette( ses )
        
        assert len( c.concept_palettes ) == 1
        assert c.concept_palettes[0] == cp
        assert len( c.palettes ) == 1
        assert c.palettes[0] == p
    
        assert len( p.concept_palettes ) == 1
        assert p.concept_palettes[0] == cp
        assert len( p.concepts ) == 1
        assert p.concepts[0] == c

        delete_concept_palette( ses )
        ses.commit()
        ses.close()
