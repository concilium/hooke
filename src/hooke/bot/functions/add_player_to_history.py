from ._function import Function

from hooke.model import HistoryPlayer

class AddPlayerToHistory( Function ):

    @property
    def name( self ):
        return 'add_player_to_history'
    
    @property
    def command_rx( self ):
        return r"^add player (?P<pid>\w+) to (?P<hid>\w+)$"

    def _process_call( self, call, session ):
        hp = HistoryPlayer( history_id = call['hid'],
                            player_id = call['pid'] )
        session.add( hp )
        session.commit()
        return '*&lt;success&gt;* added *%s* to *%s*\n' % ( call['pid'], call['hid'] )
