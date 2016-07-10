from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from . import HookeModelBase

class HistoryPlayer( HookeModelBase ):
    __tablename__ = 'historyplayer'

    # attributes
    
    history_id = Column( 'history_id', String, ForeignKey( 'history.id' ), primary_key = True )
    player_id = Column( 'player_id', String, ForeignKey( 'player.id' ), primary_key = True )
    
    # relationships
    
    history = relationship( 'History', back_populates = 'history_players' )
    player = relationship( 'Player', back_populates = 'history_players' )
    
    # miscellaneous
    
    def __repr__( self ):
        return ( "<HistoryPlayer[%s,%s]>" % ( self.history_id, self.player_id ) )
