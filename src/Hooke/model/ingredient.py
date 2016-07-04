from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from . import HookeModelBase

class Ingredient( HookeModelBase ):
    __tablename__ = 'ingredient'

    # attributes
        
    id = Column( 'id', String, primary_key = True )
    description = Column( 'description', String, nullable = False )
    
    # relationships
    
    palette_ingredients = relationship( 'PaletteIngredient', back_populates = 'ingredient' )
    palettes = association_proxy( 'palette_ingredients', 'palette' )
    
    # miscellaneous
    
    def __repr__( self ):
        return ( "<Ingredient[%s]>" % ( self.id ) )
