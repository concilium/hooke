from ._function import Function

from hooke.model import Ingredient

class DropIngredient( Function ):

    @property
    def name( self ):
        return 'drop_ingredient'
    
    @property
    def command_rx( self ):
        return r"^drop ingredient (?P<id>\w+)$"

    def _process_call( self, call, session ):
        i = session.query( Ingredient ).filter( Ingredient.id == call['id'] ).one()
        session.delete( i )
        session.commit()
        return '*&lt;success&gt;* dropped ingredient *%s*\n' % ( call['id'] )
