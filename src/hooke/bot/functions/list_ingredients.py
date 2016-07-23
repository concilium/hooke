from ._function import Function

from hooke.model import Ingredient

class ListIngredients( Function ):

    @property
    def name( self ):
        return 'list_ingredients'
    
    @property
    def command_rx( self ):
        return r"^list ingredients$"

    def _process_call( self, call, session ):
        ins = session.query( Ingredient ).all()
        if len( ins ) > 0:
            message = ''
            for i in ins:
                message += ( '<%s> %s\n' % ( i.id, i.description ) )
        else:
            message = '*(no ingredients)*\n'
        return message
