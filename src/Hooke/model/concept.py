from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from . import HookeModelBase

class Concept( HookeModelBase ):
    __tablename__ = 'concept'

    # attributes
    
    id = Column( 'id', String, primary_key = True )
    description = Column( 'description', String, nullable = False )
    
    # relationships
        
    concept_palettes = relationship( 'ConceptPalette', back_populates = 'concept' )
    palettes = association_proxy( 'concept_palettes', 'palette' )

    # miscellaneous
    
    def __repr__( self ):
        return ( "<Concept[%s]>" % ( self.id ) )
