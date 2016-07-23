from ._function import Function

class Echo( Function ):

    @property
    def name( self ):
        return 'echo'
    
    @property
    def command_rx( self ):
        return r"^echo (?P<text>.*)$"

    def _process_call( self, call, session ):
        return call['text']
