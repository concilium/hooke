from sqlalchemy import Column, String, Text
from . import HookeModelBase, tone_enum

class Scene( HookeModelBase ):
    __tablename__ = 'Scenes'
    
    # attributes
    
    id = Column( 'id', String, primary_key = True )
    tone = Column( 'tone', tone_enum )
    question = Column( 'question', String )
    narrative = Column( 'narrative', Text )
    answer = Column( 'answer', String )
    
    # relationships
    
    # miscellaneous
    
    def __repr__( self ):
        return ( "<Scene[%s]>" % ( self.id ) )
