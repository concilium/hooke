from ._function import Function

from hooke.model import Player

class ListPlayers( Function ):

    @property
    def name( self ):
        return 'list_players'
    
    @property
    def command_rx( self ):
        return r"^list players$"

    def _process_call( self, call, session ):
        ps = session.query( Player ).all()
        if len( ps ) > 0:
            message = ''
            for p in ps:
                message += ( '<%s> %s %s (%s)\n' % ( p.id, p.first_name, p.last_name, p.email ) )
        else:
            message = '*(no players)*\n'
        return message
