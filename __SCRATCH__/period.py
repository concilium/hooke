from sqlalchemy import Column, String, ForeignKey
from sqlalchemy_enum34 import EnumType

from . import HookeModelBase, Position, Tone

class Period( HookeModelBase ):
    __tablename__ = 'period'

    # attributes
    
    id = Column( 'id', String, primary_key = True )
    history_id = Column( 'history_id', String, ForeignKey( 'history.id' ), nullable = True )
    position = Column( 'position', EnumType( Position ), nullable = False )
    description = Column( 'description', String, nullable = False )
    tone = Column( 'tone', EnumType( Tone ), nullable = False )
    
    # relationships

    # miscellaneous
    
    def __repr__( self ):
        return ( "<Period[%s]>" % ( self.id ) )
