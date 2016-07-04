from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from . import HookeModelBase

class Palette( HookeModelBase ):
    __tablename__ = 'palette'

    # attributes
    
    id = Column( 'id', String, primary_key = True )
    description = Column( 'description', String, nullable = False )
    
    # relationships
    
    palette_ingredients = relationship( 'PaletteIngredient', back_populates = 'palette' )
    ingredients = association_proxy( 'palette_ingredients', 'ingredient' )

    concept_palettes = relationship( 'ConceptPalette', back_populates = 'palette' )
    concepts = association_proxy( 'concept_palettes', 'concept' )

    # miscellaneous
    
    def __repr__( self ):
        return ( "<Palette[%s]>" % ( self.id ) )



