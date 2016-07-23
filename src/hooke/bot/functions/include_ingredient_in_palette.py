from ._function import Function

from hooke.model import PaletteIngredient, Flavor

class IncludeIngredientInPalette( Function ):

    @property
    def name( self ):
        return 'include_ingredient_in_palette'
    
    @property
    def command_rx( self ):
        return r"^include ingredient (?P<iid>\w+) in (?P<pid>\w+)$"

    def _process_call( self, call, session ):
        pi = PaletteIngredient( palette_id = call['pid'],
                                ingredient_id = call['iid'],
                                flavor = Flavor.include )
        session.add( pi )
        session.commit()
        return '*&lt;success&gt;* included *%s* in *%s*\n' % ( call['iid'], call['pid'] )
