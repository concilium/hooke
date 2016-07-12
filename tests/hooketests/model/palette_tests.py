from unittest import TestCase
from nose.plugins.attrib import attr

import hooke

from ._attributes import palette_attribs
from ._helpers import check_attr, compare_attrs, check_repr

class PaletteTests( TestCase ):

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and attributes of "Palette" model class'''
    
        check_attr( hooke.model, 'Palette' )
        
        p = hooke.model.Palette( **palette_attribs )
        compare_attrs( p, palette_attribs )
        check_repr( p, p.id )
    
    @attr( type = 'persistence' )
    def test_persistence( self ):
        '''verify persistence of "Palette" instances'''
        
        ses1 = hooke.model.SQLiteMemorySession()
        p1 = hooke.model.Palette( **palette_attribs )
        ses1.add( p1 )
        ses1.commit()
        ses1.close()
    
        ses2 = hooke.model.SQLiteMemorySession()
        p2 = ses2.query( hooke.model.Palette ).filter( hooke.model.Palette.id == palette_attribs['id'] ).one()
        compare_attrs( p2, palette_attribs )
        ses2.delete( p2 )
        ses2.commit()
        ses2.close()
