from unittest import TestCase
from nose.plugins.attrib import attr

import hooke

from ._attributes import palette_attribs, ingredient_attribs, palette_ingredient_attribs
from ._helpers import check_attr, compare_attrs, check_assoc_repr

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
        
        ses1 = hooke.model.SQLiteMemorySession()
        p1 = hooke.model.Palette( **palette_attribs )
        ses1.add( p1 )
        i1 = hooke.model.Ingredient( **ingredient_attribs )
        ses1.add( i1 )
        pi1 = hooke.model.PaletteIngredient( **palette_ingredient_attribs )
        ses1.add( pi1 )
        ses1.commit()
        ses1.close()
    
        ses2 = hooke.model.SQLiteMemorySession()
        pi2 = ses2.query( hooke.model.PaletteIngredient ).filter(
                                hooke.model.PaletteIngredient.palette_id == palette_ingredient_attribs['palette_id'],
                                hooke.model.PaletteIngredient.ingredient_id == palette_ingredient_attribs['ingredient_id']
        ).one()
        compare_attrs( pi2, palette_ingredient_attribs )
        ses2.delete( pi2 )
        i2 = ses2.query( hooke.model.Ingredient ).filter( hooke.model.Ingredient.id == ingredient_attribs['id'] ).one()
        ses2.delete( i2 )
        p2 = ses2.query( hooke.model.Palette ).filter( hooke.model.Palette.id == palette_attribs['id'] ).one()
        ses2.delete( p2 )
        ses2.commit()
        ses2.close()
    
    @attr( type = 'association' )
    def test_associations( self ):
        '''verify behavior of palette_to_ingredient association'''
        
        ses = hooke.model.SQLiteMemorySession()
        p = hooke.model.Palette( **palette_attribs )
        ses.add( p )
        i = hooke.model.Ingredient( **ingredient_attribs )
        ses.add( i )
        pi = hooke.model.PaletteIngredient( **palette_ingredient_attribs )
        ses.add( pi )
        ses.commit()
        
        assert len( p.palette_ingredients ) == 1
        assert p.palette_ingredients[0] == pi
        assert len( p.ingredients ) == 1
        assert p.ingredients[0] == i
    
        assert len( i.palette_ingredients ) == 1
        assert i.palette_ingredients[0] == pi
        assert len( i.palettes ) == 1
        assert i.palettes[0] == p
    
        ses.delete( pi )
        ses.delete( i )
        ses.delete( p )
        ses.commit()
        ses.close()
