from ._function import Function

from hooke.model import Concept

class DropConcept( Function ):

    @property
    def name( self ):
        return 'drop_concept'
    
    @property
    def command_rx( self ):
        return r"^drop concept (?P<id>\w+)$"

    def _process_call( self, call, session ):
        c = session.query( Concept ).filter( Concept.id == call['id'] ).one()
        session.delete( c )
        session.commit()
        return '*&lt;success&gt;* dropped concept *%s*\n' % ( call['id'] )
