from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from . import HookeModelBase

class ConceptPalette( HookeModelBase ):
    __tablename__ = 'conceptpalette'

    # attributes
    
    concept_id = Column( 'concept_id', String, ForeignKey( 'concept.id' ), primary_key = True )
    palette_id = Column( 'palette_id', String, ForeignKey( 'palette.id' ), primary_key = True )
    title = Column( 'name', String, nullable = False )
    notes = Column( 'notes', Text, nullable = False )
    
    # relationships
    
    concept = relationship( 'Concept', back_populates = 'concept_palettes' )
    palette = relationship( 'Palette', back_populates = 'concept_palettes' )
    
    histories = relationship( 'History', back_populates = 'concept_palette' )

    # miscellaneous
    
    def __repr__( self ):
        return ( "<ConceptPalette[%s,%s]>" % ( self.concept_id, self.palette_id ) )
