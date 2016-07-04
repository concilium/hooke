from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_enum34 import EnumType

from . import HookeModelBase, Flavor

class PaletteIngredient( HookeModelBase ):
    __tablename__ = 'paletteingredient'

    # attributes
        
    palette_id = Column( 'palette_id', String, ForeignKey( 'palette.id' ), primary_key = True )
    ingredient_id = Column( 'ingredient_id', String, ForeignKey( 'ingredient.id' ), primary_key = True )
    flavor = Column( 'flavor', EnumType( Flavor ), nullable = False )
    
    # relationships
    
    palette = relationship( 'Palette', back_populates = 'palette_ingredients' )
    ingredient = relationship( 'Ingredient', back_populates = 'palette_ingredients' )

    # miscellaneous
    
    def __repr__( self ):
        return ( "<PaletteIngredient[%s,%s]>" % ( self.palette_id, self.ingredient_id ) )
