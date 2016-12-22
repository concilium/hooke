from ._function import Function

from hooke.model import History, State

class ListHistories( Function ):

    @property
    def name( self ):
        return 'list_histories'
    
    @property
    def command_rx( self ):
        return r"^list histories$"

    def _process_call( self, call, session ):
        hs = session.query( History ).all()
        if len( hs ) > 0:
            message = ''
            for h in hs:
                if h.state == State.active:
                    message += ( '<%s> %s\n' % ( h.id, h.title ) )
                elif h.state == State.inactive:
                    message += ( '_<%s> %s_\n' % ( h.id, h.title ) )
        else:
            message = '*(no histories)*\n'
        return message
