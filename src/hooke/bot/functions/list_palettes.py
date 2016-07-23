from ._function import Function

from hooke.model import Palette

class ListPalettes( Function ):

    @property
    def name( self ):
        return 'list_palettes'
    
    @property
    def command_rx( self ):
        return r"^list palettes$"

    def _process_call( self, call, session ):
        ps = session.query( Palette ).all()
        if len( ps ) > 0:
            message = ''
            for p in ps:
                message += ( '<%s> %s\n' % ( p.id, p.description ) )
        else:
            message = '*(no palettes)*\n'
        return message
