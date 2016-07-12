from unittest import TestCase
from nose.plugins.attrib import attr

import hooke

from ._attributes import history_attribs, concept_attribs, palette_attribs, concept_palette_attribs
from ._helpers import check_attr, compare_attrs, check_repr

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
        
        ses1 = hooke.model.SQLiteMemorySession()
        c1 = hooke.model.Concept( **concept_attribs )
        ses1.add( c1 )
        p1 = hooke.model.Palette( **palette_attribs )
        ses1.add( p1 )
        cp1 = hooke.model.ConceptPalette( **concept_palette_attribs )
        ses1.add( cp1 )
        h1 = hooke.model.History( **history_attribs )
        ses1.add( h1 )
        ses1.commit()
        ses1.close()
        
        ses2 = hooke.model.SQLiteMemorySession()
        h2 = ses2.query( hooke.model.History ).filter( hooke.model.History.id == history_attribs['id'] ).one()
        compare_attrs( h2, history_attribs )
        ses2.delete( h2 )
        cp2 = ses2.query( hooke.model.ConceptPalette ).filter(
                            hooke.model.ConceptPalette.concept_id == concept_palette_attribs['concept_id'],
                            hooke.model.ConceptPalette.palette_id == concept_palette_attribs['palette_id']
        ).one()
        ses2.delete( cp2 )
        p2 = ses2.query( hooke.model.Palette ).filter( hooke.model.Palette.id == palette_attribs['id'] ).one()
        ses2.delete( p2 )
        c2 = ses2.query( hooke.model.Concept ).filter( hooke.model.Concept.id == concept_attribs['id'] ).one()
        ses2.delete( c2 )
        ses2.commit()
        ses2.close()
