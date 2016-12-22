from ._function import Function

from hooke.model import ConceptPalette

class ListSeeds( Function ):

    @property
    def name( self ):
        return 'list_seeds'
    
    @property
    def command_rx( self ):
        return r"^list seeds$"

    def _process_call( self, call, session ):
        cps = session.query( ConceptPalette ).all()
        if len( cps ) > 0:
            message = ''
            for cp in cps:
                message += ( '<%s|%s> %s\n' % ( cp.concept_id, cp.palette_id, cp.title ) )
        else:
            message = '*(no seeds)*\n'
        return message
