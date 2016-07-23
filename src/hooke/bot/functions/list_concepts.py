from ._function import Function

from hooke.model import Concept

class ListConcepts( Function ):

    @property
    def name( self ):
        return 'list_concepts'
    
    @property
    def command_rx( self ):
        return r"^list concepts$"

    def _process_call( self, call, session ):
        cs = session.query( Concept ).all()
        if len( cs ) > 0:
            message = ''
            for c in cs:
                message += ( '<%s> %s\n' % ( c.id, c.description ) )
        else:
            message = '*(no concepts)*\n'
        return message
