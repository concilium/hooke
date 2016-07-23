from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from . import HookeModelBase

class Player( HookeModelBase ):
    __tablename__ = 'player'

    # attributes
        
    id = Column( 'id', String, primary_key = True )
    first_name = Column( 'first_name', String, nullable = False  )
    last_name = Column( 'last_name', String, nullable = False  )
    email = Column( 'email', String, nullable = False  )
    
    # relationships

    history_players = relationship( 'HistoryPlayer', back_populates = 'player' )
    histories = association_proxy( 'history_players', 'history' )
        
    # miscellaneous
    
    def __repr__( self ):
        return ( "<Player[%s]>" % ( self.id ) )
