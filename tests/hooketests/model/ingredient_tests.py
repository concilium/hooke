from unittest import TestCase
from nose.plugins.attrib import attr

import hooke

from ._factory import ingredient_attribs, add_ingredient, query_ingredient, delete_ingredient
from ._helpers import check_attr, compare_attrs, check_repr

class IngredientTests( TestCase ):

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and attributes of "Ingredient" model class'''
    
        check_attr( hooke.model, 'Ingredient' )
        
        i = hooke.model.Ingredient( **ingredient_attribs )
        compare_attrs( i, ingredient_attribs )
        check_repr( i, i.id )
    
    @attr( type = 'persistence' )
    def test_persistence( self ):
        '''verify persistence of "Ingredient" instances'''
        
        ses1 = hooke.model.SQLiteMemorySession()
        add_ingredient( ses1 )
        ses1.commit()
        ses1.close()
    
        ses2 = hooke.model.SQLiteMemorySession()
        i = query_ingredient( ses2 )
        compare_attrs( i, ingredient_attribs )
        delete_ingredient( ses2 )
        ses2.commit()
        ses2.close()
