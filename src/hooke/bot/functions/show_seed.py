from ._function import Function

from hooke.model import ConceptPalette, Flavor

class ShowSeed( Function ):

    @property
    def name( self ):
        return 'show_seed'
    
    @property
    def command_rx( self ):
        return r"^show seed (?P<cid>\w+)\|(?P<pid>\w+)$"

    def _process_call( self, call, session ):
        cp = session.query( ConceptPalette ).filter( ConceptPalette.concept_id == call['cid'],
                                                     ConceptPalette.palette_id == call['pid'] ).one()
        message = '*&lt;seed:%s|%s&gt;*\n' % ( cp.concept_id, cp.palette_id )
        message += '*Title:* %s\n' % ( cp.title )
        message += '*Concept:* %s\n' % ( cp.concept.description )
        message += '*Palette:* %s\n' % ( cp.palette.description )
        message += '*Notes:* %s\n' % ( cp.notes )
#        message += '*Ingredients:*\n'
#        for pi in cp.palette.palette_ingredients:
#            if pi.flavor == Flavor.include:
#                message += '  *+* %s\n' % ( pi.ingredient.description )
#            elif pi.flavor == Flavor.exclude:
#                message += '  *-* %s\n' % ( pi.ingredient.description )
#            else:
#                pass    #### should never happen
        return message
