from ._function import Function

from hooke.model import Ingredient

class MakeIngredient( Function ):

    @property
    def name( self ):
        return 'make_ingredient'
    
    @property
    def command_rx( self ):
        return r"^make ingredient \"(?P<description>.*?)\" as (?P<id>\w+)$"

    def _process_call( self, call, session ):
        i = Ingredient( id = call['id'], description = call['description'] )
        session.add( i )
        session.commit()
        return '*&lt;success&gt;* made ingredient *%s*\n' % ( call['id'] )
