import Hooke

from ._attributes import palette_attribs, ingredient_attribs, palette_ingredient_attribs
from ._helpers import check_attr, compare_attrs, check_assoc_repr

def test_palette_ingredient_model():
    '''verify existence and attributes of "PaletteIngredient" model class'''

    check_attr( Hooke.model, 'PaletteIngredient' )
    
    pi = Hooke.model.PaletteIngredient( **palette_ingredient_attribs )
    compare_attrs( pi, palette_ingredient_attribs )
    check_assoc_repr( pi, pi.palette_id, pi.ingredient_id )

def test_palette_ingredient_persistence():
    '''verify persistence of "PaletteIngredient" instances'''
    
    ses1 = Hooke.model.SQLiteMemorySession()
    p1 = Hooke.model.Palette( **palette_attribs )
    ses1.add( p1 )
    i1 = Hooke.model.Ingredient( **ingredient_attribs )
    ses1.add( i1 )
    pi1 = Hooke.model.PaletteIngredient( **palette_ingredient_attribs )
    ses1.add( pi1 )
    ses1.commit()
    ses1.close()

    ses2 = Hooke.model.SQLiteMemorySession()
    pi2 = ses2.query( Hooke.model.PaletteIngredient ).filter(
                            Hooke.model.PaletteIngredient.palette_id == palette_ingredient_attribs['palette_id'],
                            Hooke.model.PaletteIngredient.ingredient_id == palette_ingredient_attribs['ingredient_id']
    ).one()
    compare_attrs( pi2, palette_ingredient_attribs )
    ses2.delete( pi2 )
    i2 = ses2.query( Hooke.model.Ingredient ).filter( Hooke.model.Ingredient.id == ingredient_attribs['id'] ).one()
    ses2.delete( i2 )
    p2 = ses2.query( Hooke.model.Palette ).filter( Hooke.model.Palette.id == palette_attribs['id'] ).one()
    ses2.delete( p2 )
    ses2.commit()
    ses2.close()

def test_palette_ingredient_association():
    '''verify behavior of palette_to_ingredient association'''
    
    ses = Hooke.model.SQLiteMemorySession()
    p = Hooke.model.Palette( **palette_attribs )
    ses.add( p )
    i = Hooke.model.Ingredient( **ingredient_attribs )
    ses.add( i )
    pi = Hooke.model.PaletteIngredient( **palette_ingredient_attribs )
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
