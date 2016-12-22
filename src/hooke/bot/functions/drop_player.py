from ._function import Function

from hooke.model import Player

class DropPlayer( Function ):

    @property
    def name( self ):
        return 'drop_player'
    
    @property
    def command_rx( self ):
        return r"^drop player (?P<id>\w+)$"

    def _process_call( self, call, session ):
        p = session.query( Player ).filter( Player.id == call['id'] ).one()
        session.delete( p )
        session.commit()
        return '*&lt;success&gt;* dropped player *%s*\n' % ( call['id'] )
