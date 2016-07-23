from ._function import Function

from hooke.model import Palette

class DropPalette( Function ):

    @property
    def name( self ):
        return 'drop_palette'
    
    @property
    def command_rx( self ):
        return r"^drop palette (?P<id>\w+)$"

    def _process_call( self, call, session ):
        p = session.query( Palette ).filter( Palette.id == call['id'] ).one()
        session.delete( p )
        session.commit()
        return '*&lt;success&gt;* dropped palette *%s*\n' % ( call['id'] )
