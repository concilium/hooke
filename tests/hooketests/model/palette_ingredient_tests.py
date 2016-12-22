from unittest import TestCase
from nose.plugins.attrib import attr

import hooke

from ._factory import palette_ingredient_attribs, add_palette_ingredient, query_palette_ingredient, delete_palette_ingredient, query_palette, query_ingredient
from ._helpers import check_attr, compare_attrs, check_assoc_repr, SQLiteMemorySession

class PaletteIngredientTests( TestCase ):

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and attributes of "PaletteIngredient" model class'''
    
        check_attr( hooke.model, 'PaletteIngredient' )
        
        pi = hooke.model.PaletteIngredient( **palette_ingredient_attribs )
        compare_attrs( pi, palette_ingredient_attribs )
        check_assoc_repr( pi, pi.palette_id, pi.ingredient_id )

    @attr( type = 'persistence' )
    def test_persistence( self ):
        '''verify persistence of "PaletteIngredient" instances'''
        
        ses1 = SQLiteMemorySession()
        add_palette_ingredient( ses1 )
        ses1.commit()
        ses1.close()
    
        ses2 = SQLiteMemorySession()
        pi = query_palette_ingredient( ses2 )
        compare_attrs( pi, palette_ingredient_attribs )
        delete_palette_ingredient( ses2 )
        ses2.commit()
        ses2.close()
    
    @attr( type = 'association' )
    def test_associations( self ):
        '''verify behavior of palette-to-ingredient association'''
        
        ses = SQLiteMemorySession()
        add_palette_ingredient( ses )
        ses.commit()

        p = query_palette( ses )
        i = query_ingredient( ses )
        pi = query_palette_ingredient( ses )
        
        assert len( p.palette_ingredients ) == 1
        assert p.palette_ingredients[0] == pi
        assert len( p.ingredients ) == 1
        assert p.ingredients[0] == i
    
        assert len( i.palette_ingredients ) == 1
        assert i.palette_ingredients[0] == pi
        assert len( i.palettes ) == 1
        assert i.palettes[0] == p

        delete_palette_ingredient( ses )
        ses.commit()
        ses.close()
