from sqlalchemy import Column, String, DateTime, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy_enum34 import EnumType

from . import HookeModelBase, State

class History( HookeModelBase ):
    __tablename__ = 'history'
    __table_args__ = (
        ForeignKeyConstraint( [ 'concept_id', 'palette_id' ],
                              [ 'conceptpalette.concept_id', 'conceptpalette.palette_id' ] ),
    )

    # attributes
        
    id = Column( 'id', String, primary_key = True )
    started_on = Column( 'started_on', DateTime, nullable = False  )
    concept_id = Column( 'concept_id', String, nullable = False )
    palette_id = Column( 'palette_id', String, nullable = False )
    state = Column( 'state', EnumType( State ), nullable = False )

    # relationships
    
    concept_palette = relationship( 'ConceptPalette', back_populates = 'histories' )
    
    # miscellaneous
    
    def __repr__( self ):
        return ( "<History[%s]>" % ( self.id ) )
