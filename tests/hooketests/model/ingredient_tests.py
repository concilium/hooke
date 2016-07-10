from nose.plugins.attrib import attr

import Hooke

from ._attributes import ingredient_attribs
from ._helpers import check_attr, compare_attrs, check_repr

class IngredientTests:

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and attributes of "Ingredient" model class'''
    
        check_attr( Hooke.model, 'Ingredient' )
        
        i = Hooke.model.Ingredient( **ingredient_attribs )
        compare_attrs( i, ingredient_attribs )
        check_repr( i, i.id )
    
    @attr( type = 'persistence' )
    def test_persistence( self ):
        '''verify persistence of "Ingredient" instances'''
        
        ses1 = Hooke.model.SQLiteMemorySession()
        i1 = Hooke.model.Ingredient( **ingredient_attribs )
        ses1.add( i1 )
        ses1.commit()
        ses1.close()
    
        ses2 = Hooke.model.SQLiteMemorySession()
        i2 = ses2.query( Hooke.model.Ingredient ).filter( Hooke.model.Ingredient.id == ingredient_attribs['id'] ).one()
        compare_attrs( i2, ingredient_attribs )
        ses2.delete( i2 )
        ses2.commit()
        ses2.close()
