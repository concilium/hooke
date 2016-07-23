from ._function import Function

from hooke.model import Palette

class MakePalette( Function ):

    @property
    def name( self ):
        return 'make_palette'
    
    @property
    def command_rx( self ):
        return r"^make palette \"(?P<description>.*?)\" as (?P<id>\w+)$"

    def _process_call( self, call, session ):
        p = Palette( id = call['id'], description = call['description'] )
        session.add( p )
        session.commit()
        return '*&lt;success&gt;* made palette *%s*\n' % ( call['id'] )
