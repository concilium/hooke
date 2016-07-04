from sqlalchemy import Column, String
from . import HookeModelBase, tone_enum

class Event( HookeModelBase ):
    __tablename__ = 'Events'
    
    # attributes
    
    id = Column( 'id', String, primary_key = True )
    tone = Column( 'tone', tone_enum )
    description = Column( 'description', String )
    
    # relationships
    
    # miscellaneous
    
    def __repr__( self ):
        return ( "<Event[%s]>" % ( self.id ) )
