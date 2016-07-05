import Hooke

from ._attributes import palette_attribs
from ._helpers import check_attr, compare_attrs, check_repr

def test_palette_model():
    '''verify existence and attributes of "Palette" model class'''

    check_attr( Hooke.model, 'Palette' )
    
    p = Hooke.model.Palette( **palette_attribs )
    compare_attrs( p, palette_attribs )
    check_repr( p, p.id )

def test_palette_persistence():
    '''verify persistence of "Palette" instances'''
    
    ses1 = Hooke.model.SQLiteMemorySession()
    p1 = Hooke.model.Palette( **palette_attribs )
    ses1.add( p1 )
    ses1.commit()
    ses1.close()

    ses2 = Hooke.model.SQLiteMemorySession()
    p2 = ses2.query( Hooke.model.Palette ).filter( Hooke.model.Palette.id == palette_attribs['id'] ).one()
    compare_attrs( p2, palette_attribs )
    ses2.delete( p2 )
    ses2.commit()
    ses2.close()
