from contextlib import contextmanager
from datetime import datetime
from pydispatch import dispatcher

from hooke.model import Concept, Palette, Ingredient, ConceptPalette, PaletteIngredient, History, Player
from hooke.model import Flavor, State
from .wiring import Senders, Signals

@contextmanager
def new_session( session_factory ):
    session = session_factory()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    
class Executive:

    def __init__( self, session_factory ):

        self.sender_name = Senders.EXECUTIVE
        self.session_factory = session_factory
        
        dispatcher.connect( self.echo_handler, Signals.ECHO, dispatcher.Any )
        dispatcher.connect( self.make_concept_handler, Signals.MAKE_CONCEPT, dispatcher.Any )
        dispatcher.connect( self.list_concepts_handler, Signals.LIST_CONCEPTS, dispatcher.Any )
        dispatcher.connect( self.make_palette_handler, Signals.MAKE_PALETTE, dispatcher.Any )
        dispatcher.connect( self.list_palettes_handler, Signals.LIST_PALETTES, dispatcher.Any )
        dispatcher.connect( self.make_ingredient_handler, Signals.MAKE_INGREDIENT, dispatcher.Any )
        dispatcher.connect( self.list_ingredients_handler, Signals.LIST_INGREDIENTS, dispatcher.Any )
        dispatcher.connect( self.include_ingredient_in_palette_handler, Signals.INCLUDE_INGREDIENT_IN_PALETTE, dispatcher.Any )
        dispatcher.connect( self.exclude_ingredient_in_palette_handler, Signals.EXCLUDE_INGREDIENT_IN_PALETTE, dispatcher.Any )
        dispatcher.connect( self.remove_ingredient_from_palette_handler, Signals.REMOVE_INGREDIENT_FROM_PALETTE, dispatcher.Any )
        dispatcher.connect( self.create_seed_handler, Signals.CREATE_SEED, dispatcher.Any )
        dispatcher.connect( self.list_seeds_handler, Signals.LIST_SEEDS, dispatcher.Any )
        dispatcher.connect( self.show_seed_handler, Signals.SHOW_SEED, dispatcher.Any )
        dispatcher.connect( self.start_history_handler, Signals.START_HISTORY, dispatcher.Any )
        dispatcher.connect( self.list_histories_handler, Signals.LIST_HISTORIES, dispatcher.Any )
        dispatcher.connect( self.show_history_handler, Signals.SHOW_HISTORY, dispatcher.Any )
        dispatcher.connect( self.make_player_handler, Signals.MAKE_PLAYER, dispatcher.Any )
        dispatcher.connect( self.list_players_handler, Signals.LIST_PLAYERS, dispatcher.Any )
    
    def _dispatch_message( self, message ):
    
        dispatcher.send( signal = Signals.POST_MESSAGE,
                         sender = self.sender_name,
                         message = message )
    
    def echo_handler( self, sender, message ):

        self._dispatch_message( message )

    def make_concept_handler( self, sender, cid, description ):
        
        with new_session( self.session_factory ) as ses:
            c = Concept( id = cid, description = description )
            ses.add( c )
            
        self._dispatch_message( 'created %s' % ( cid ) )
        
    def list_concepts_handler( self, sender ):

        message = 'Concepts:\n'
        with new_session( self.session_factory ) as ses:
            concepts = ses.query( Concept ).all()
            if len( concepts ) > 0:
                for c in concepts:
                    message += ( '[%s] %s\n' % ( c.id, c.description ) )
            else:
                message = '(no concepts)\n'
    
        self._dispatch_message( message )
    
    def make_palette_handler( self, sender, pid, description ):
        
        with new_session( self.session_factory ) as ses:
            p = Palette( id = pid, description = description )
            ses.add( p )
            
        self._dispatch_message( 'created %s' % ( pid ) )
        
    def list_palettes_handler( self, sender ):

        message = 'Palettes:\n'
        with new_session( self.session_factory ) as ses:
            palettes = ses.query( Palette ).all()
            if len( palettes ) > 0:
                for p in palettes:
                    message += ( '[%s] %s\n' % ( p.id, p.description ) )
            else:
                message = '(no palettes)\n'
    
        self._dispatch_message( message )
    
    def make_ingredient_handler( self, sender, iid, description ):
        
        with new_session( self.session_factory ) as ses:
            i = Ingredient( id = iid, description = description )
            ses.add( i )
            
        self._dispatch_message( 'created %s' % ( iid ) )
        
    def list_ingredients_handler( self, sender ):

        message = 'Ingredients:\n'
        with new_session( self.session_factory ) as ses:
            ingredients = ses.query( Ingredient ).all()
            if len( ingredients ) > 0:
                for i in ingredients:
                    message += ( '[%s] %s\n' % ( i.id, i.description ) )
            else:
                message = '(no ingredients)\n'
    
        self._dispatch_message( message )

    def include_ingredient_in_palette_handler( self, sender, iid, pid ):

        with new_session( self.session_factory ) as ses:
            pi = PaletteIngredient( palette_id = pid, ingredient_id = iid, flavor = Flavor.include )
            ses.add( pi )

        self._dispatch_message( 'included %s in %s' % ( iid, pid ) )

    def exclude_ingredient_in_palette_handler( self, sender, iid, pid ):

        with new_session( self.session_factory ) as ses:
            pi = PaletteIngredient( palette_id = pid, ingredient_id = iid, flavor = Flavor.exclude )
            ses.add( pi )

        self._dispatch_message( 'excluded %s in %s' % ( iid, pid ) )

    def remove_ingredient_from_palette_handler( self, sender, iid, pid ):

        with new_session( self.session_factory ) as ses:
            pi = ses.query( PaletteIngredient ).filter( PaletteIngredient.palette_id == pid, PaletteIngredient.ingredient_id == iid ).one()
            ses.delete( pi )

        self._dispatch_message( 'removed %s from %s' % ( iid, pid ) )
        
    def create_seed_handler( self, sender, cid, pid, title, notes ):
        
        with new_session( self.session_factory ) as ses:
            cp = ConceptPalette( concept_id = cid, palette_id = pid, title = title, notes = notes )
            ses.add( cp )
            
        self._dispatch_message( 'created %s|%s' % ( cid, pid ) )
        
    def list_seeds_handler( self, sender ):
        
        message = 'Seeds:\n'
        with new_session( self.session_factory ) as ses:
            conceptpalettes = ses.query( ConceptPalette ).all()
            if len( conceptpalettes ) > 0:
                for cp in conceptpalettes:
                    message += ( '[%s|%s] %s\n' % ( cp.concept_id, cp.palette_id, cp.title ) )
            else:
                message = '(no seeds)\n'

        self._dispatch_message( message )

    def show_seed_handler( self, sender, cid, pid ):
        
        message = ''
        with new_session( self.session_factory ) as ses:
            cp = ses.query( ConceptPalette ).filter( ConceptPalette.concept_id == cid, ConceptPalette.palette_id == pid ).one()
            message += '*"%s"*\n' % ( cp.title )
            message += '*Concept:* %s\n' % ( cp.concept.description )
            message += '*Palette:*\n'
            for pi in cp.palette.palette_ingredients:
                if pi.flavor == Flavor.include:
                    message += '> *+* '
                elif pi.flavor == Flavor.exclude:
                    message += '> *-* '
                else:
                    message += '> *?* '         # should never happen, raise exception instead?
                message += '%s\n' % ( pi.ingredient.description )
            message += '*Notes:* %s\n' % ( cp.notes )
            
        self._dispatch_message( message )
        
    def start_history_handler( self, sender, hid, title, cid, pid ):
        
        with new_session( self.session_factory ) as ses:
            h = History( id = hid,
                         title = title,
                         concept_id = cid,
                         palette_id = pid,
                         started_on = datetime.now(),
                         state = State.active )
            ses.add( h )
            
        self._dispatch_message( 'started %s' % ( hid ) )
    
    def list_histories_handler( self, sender ):
        
        message = 'Histories:\n'
        with new_session( self.session_factory ) as ses:
            histories = ses.query( History ).all()
            if len( histories ) > 0:
                for h in histories:
                    if h.state == State.active:
                        message += ( '*[%s]* %s\n' % ( h.id, h.title ) )
                    elif h.state == State.inactive:
                        message += ( '[%s] %s\n' % ( h.id, h.title ) )
                    else:
                        pass         # should never happen, raise exception instead?
            else:
                message = '(no histories)\n'

        self._dispatch_message( message )

    def show_history_handler( self, sender, hid ):

        message = ''
        with new_session( self.session_factory ) as ses:
            h = ses.query( History ).filter( History.id == hid ).one()
            message += '*"%s"*\n' % ( h.title )
            message += '*Seed:% %s\n' % ( h.concept_palette.title )
            message += '*Started:* %s\n' % ( h.started_on )
            message += '*State:* %s\n' % ( h.state )
            message += '*Players:*\n'
            if len( h.players ) > 0:
                for p in h.players:
                    message += '> %s %s\n' % ( p.first_name, p.last_name )
            else:
                message += '(no players)\n'
            
        self._dispatch_message( message )

    def make_player_handler( self, sender, pid, fname, lname, email ):

        with new_session( self.session_factory ) as ses:
            p = Player( id = pid, first_name = fname, last_name = lname, email = email )
            ses.add( p )
            
        self._dispatch_message( 'added %s' % ( pid ) )

    def list_players_handler( self, sender ):
        
        message = 'Players:\n'
        with new_session( self.session_factory ) as ses:
            players = ses.query( Player ).all()
            if len( players ) > 0:
                for p in players:
                    message += ( '[%s] %s %s <%s>\n' % ( p.id, p.first_name, p.last_name, p.email ) )
            else:
                message = '(no players)\n'
    
        self._dispatch_message( message )
