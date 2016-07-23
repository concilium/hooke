from ._function import Function

from hooke.model import Concept

class MakeConcept( Function ):

    @property
    def name( self ):
        return 'make_concept'
    
    @property
    def command_rx( self ):
        return r"^make concept \"(?P<description>.*?)\" as (?P<id>\w+)$"

    def _process_call( self, call, session ):
        c = Concept( id = call['id'], description = call['description'] )
        session.add( c )
        session.commit()
        return '*&lt;success&gt;* made concept *%s*\n' % ( call['id'] )
