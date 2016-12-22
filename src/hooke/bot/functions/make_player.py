from ._function import Function

from hooke.model import Player

class MakePlayer( Function ):

    @property
    def name( self ):
        return 'make_player'
    
    @property
    def command_rx( self ):
        return r"^make player (?P<first_name>.*?) (?P<last_name>.*?) \((?P<email>.*?)\) as (?P<id>\w+)$"

    def _process_call( self, call, session ):
        p = Player( id = call['id'], first_name = call['first_name'],
                    last_name = call['last_name'], email = call['email'] )
        session.add( p )
        session.commit()
        return '*&lt;success&gt;* made player *%s*\n' % ( call['id'] )
