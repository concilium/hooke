from unittest import TestCase
from nose.plugins.attrib import attr

import hooke

from ._factory import palette_attribs, add_palette, query_palette, delete_palette
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
        add_palette( ses1 )
        ses1.commit()
        ses1.close()
    
        ses2 = hooke.model.SQLiteMemorySession()
        p = query_palette( ses2 )
        compare_attrs( p, palette_attribs )
        delete_palette( ses2 )
        ses2.commit()
        ses2.close()
