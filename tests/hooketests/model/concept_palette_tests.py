from nose.plugins.attrib import attr

import Hooke

from ._attributes import concept_attribs, palette_attribs, concept_palette_attribs
from ._helpers import check_attr, compare_attrs, check_assoc_repr

class ConceptPaletteTests:

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and attributes of "ConceptPalette" model class'''
    
        check_attr( Hooke.model, 'ConceptPalette' )
        
        cp = Hooke.model.ConceptPalette( **concept_palette_attribs )
        compare_attrs( cp, concept_palette_attribs )
        check_assoc_repr( cp, cp.concept_id, cp.palette_id )
    
    @attr( type = 'persistence' )
    def test_persistence( self ):
        '''verify persistence of "ConceptPalette" instances'''
        
        ses1 = Hooke.model.SQLiteMemorySession()
        c1 = Hooke.model.Concept( **concept_attribs )
        ses1.add( c1 )
        p1 = Hooke.model.Palette( **palette_attribs )
        ses1.add( p1 )
        cp1 = Hooke.model.ConceptPalette( **concept_palette_attribs )
        ses1.add( cp1 )
        ses1.commit()
        ses1.close()
    
        ses2 = Hooke.model.SQLiteMemorySession()
        cp2 = ses2.query( Hooke.model.ConceptPalette ).filter(
                                Hooke.model.ConceptPalette.concept_id == concept_palette_attribs['concept_id'],
                                Hooke.model.ConceptPalette.palette_id == concept_palette_attribs['palette_id']
        ).one()
        compare_attrs( cp2, concept_palette_attribs )
        ses2.delete( cp2 )
        p2 = ses2.query( Hooke.model.Palette ).filter( Hooke.model.Palette.id == palette_attribs['id'] ).one()
        ses2.delete( p2 )
        c2 = ses2.query( Hooke.model.Concept ).filter( Hooke.model.Concept.id == concept_attribs['id'] ).one()
        ses2.delete( c2 )
        ses2.commit()
        ses2.close()
    
    @attr( type = 'association' )
    def test_associations( self ):
        '''verify behavior of concept-to-palette association'''
        
        ses = Hooke.model.SQLiteMemorySession()
        c = Hooke.model.Concept( **concept_attribs )
        ses.add( c )
        p = Hooke.model.Palette( **palette_attribs )
        ses.add( p )
        cp = Hooke.model.ConceptPalette( **concept_palette_attribs )
        ses.add( cp )
        ses.commit()
        
        assert len( c.concept_palettes ) == 1
        assert c.concept_palettes[0] == cp
        assert len( c.palettes ) == 1
        assert c.palettes[0] == p
    
        assert len( p.concept_palettes ) == 1
        assert p.concept_palettes[0] == cp
        assert len( p.concepts ) == 1
        assert p.concepts[0] == c
    
        ses.delete( cp )
        ses.delete( p )
        ses.delete( c )
        ses.commit()
        ses.close()
