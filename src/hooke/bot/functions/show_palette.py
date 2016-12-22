from ._function import Function

from hooke.model import Palette, Flavor

class ShowPalette( Function ):

    @property
    def name( self ):
        return 'show_palette'
    
    @property
    def command_rx( self ):
        return r"^show palette (?P<id>\w+)$"

    def _process_call( self, call, session ):
        p = session.query( Palette ).filter( Palette.id == call['id'] ).one()
        message = '*&lt;palette:%s&gt;*\n' % ( p.id )
        message += '*Description:* %s\n' % ( p.description )
        message += '*Ingredients:*\n'
        for pi in p.palette_ingredients:
            if pi.flavor == Flavor.include:
                message += '  *+* %s\n' % ( pi.ingredient.description )
            elif pi.flavor == Flavor.exclude:
                message += '  *-* %s\n' % ( pi.ingredient.description )
            else:
                pass    #### should never happen
        return message
