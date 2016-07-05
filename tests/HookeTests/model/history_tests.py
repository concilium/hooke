import Hooke

from ._attributes import history_attribs, concept_attribs, palette_attribs, concept_palette_attribs
from ._helpers import check_attr, compare_attrs, check_repr

def test_history_model():
    '''verify existence and attributes of "History" model class'''

    check_attr( Hooke.model, 'History' )
    
    h = Hooke.model.History( **history_attribs )
    compare_attrs( h, history_attribs )
    check_repr( h, h.id )

def test_history_persistence():
    '''verify persistence of "History" instances'''
    
    ses1 = Hooke.model.SQLiteMemorySession()
    c1 = Hooke.model.Concept( **concept_attribs )
    ses1.add( c1 )
    p1 = Hooke.model.Palette( **palette_attribs )
    ses1.add( p1 )
    cp1 = Hooke.model.ConceptPalette( **concept_palette_attribs )
    ses1.add( cp1 )
    h1 = Hooke.model.History( **history_attribs )
    ses1.add( h1 )
    ses1.commit()
    ses1.close()
    
    ses2 = Hooke.model.SQLiteMemorySession()
    h2 = ses2.query( Hooke.model.History ).filter( Hooke.model.History.id == history_attribs['id'] ).one()
    compare_attrs( h2, history_attribs )
    ses2.delete( h2 )
    cp2 = ses2.query( Hooke.model.ConceptPalette ).filter(
                        Hooke.model.ConceptPalette.concept_id == concept_palette_attribs['concept_id'],
                        Hooke.model.ConceptPalette.palette_id == concept_palette_attribs['palette_id']
    ).one()
    ses2.delete( cp2 )
    p2 = ses2.query( Hooke.model.Palette ).filter( Hooke.model.Palette.id == palette_attribs['id'] ).one()
    ses2.delete( p2 )
    c2 = ses2.query( Hooke.model.Concept ).filter( Hooke.model.Concept.id == concept_attribs['id'] ).one()
    ses2.delete( c2 )
    ses2.commit()
    ses2.close()
