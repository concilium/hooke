from ._function import Function

from hooke.model import History, Flavor

class ShowHistory( Function ):

    @property
    def name( self ):
        return 'show_history'
    
    @property
    def command_rx( self ):
        return r"^show history (?P<id>\w+)$"

    def _process_call( self, call, session ):
        h = session.query( History ).filter( History.id == call['id'] ).one()
        message = '*&lt;history:%s[%s]&gt;*\n' % ( h.id, h.state.name )
        message += '*Title:* %s\n' % ( h.title )
        message += '*Started:* %s\n' % ( h.started_on.strftime( '%x' ) )
        message += '*Concept:* %s\n' % ( h.concept.description )
        message += '*Palette:*\n'
        for pi in h.palette.palette_ingredients:
            if pi.flavor == Flavor.include:
                message += '  *+* %s\n' % ( pi.ingredient.description )
            elif pi.flavor == Flavor.exclude:
                message += '  *-* %s\n' % ( pi.ingredient.description )
            else:
                pass    #### should never happen
        message += '*Players:*\n'
        for p in h.players:
            message += '  *+* %s %s (%s)\n' % ( p.first_name, p.last_name, p.email )
        return message
