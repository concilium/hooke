from ._function import Function

from hooke.model import PaletteIngredient

class RemoveIngredientFromPalette( Function ):

    @property
    def name( self ):
        return 'remove_ingredient_from_palette'
    
    @property
    def command_rx( self ):
        return r"^remove ingredient (?P<iid>\w+) from (?P<pid>\w+)$"

    def _process_call( self, call, session ):
        pi = session.query( PaletteIngredient ).filter( 
                    PaletteIngredient.palette_id == call['pid'],
                    PaletteIngredient.ingredient_id == call['iid'] ).one()
        session.delete( pi )
        session.commit()
        return '*&lt;success&gt;* removed *%s* from *%s*\n' % ( call['iid'], call['pid'] )
