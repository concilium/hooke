import logging
import queue

from sqlalchemy.orm import scoped_session, sessionmaker

from .listener import Listener
from .emitter import Emitter
from .mapper import Mapper

from .functions import Echo
from .functions import MakeConcept, DropConcept, ListConcepts
from .functions import MakePalette, DropPalette, ListPalettes
from .functions import MakeIngredient, DropIngredient, ListIngredients
from .functions import IncludeIngredientInPalette, ExcludeIngredientInPalette, RemoveIngredientFromPalette

class Chassis:

    def __init__( self, slack_bot_token, slack_bot_name, slack_channel_name, sqla_engine ):
        self._log = logging.getLogger( 'hooke.bot.Chassis' )
        self._log.info( 'chassis initializing' )

        self.command_q = queue.Queue()
        self.listener = Listener( slack_bot_token = slack_bot_token,
                                  slack_bot_name = slack_bot_name,
                                  slack_channel_name = slack_channel_name,
                                  command_q = self.command_q )
        
        self.message_q = queue.Queue()
        self.emitter = Emitter( slack_bot_token = slack_bot_token,
                                slack_bot_name = slack_bot_name,
                                slack_channel_name = slack_channel_name,
                                message_q = self.message_q )

        self.session_factory = sessionmaker( bind = sqla_engine )
        self.session = scoped_session( self.session_factory )
        
        self.mapper = Mapper( command_q = self.command_q )

        for Function in [ Echo,
                          MakeConcept, DropConcept, ListConcepts,
                          MakePalette, DropPalette, ListPalettes,
                          MakeIngredient, DropIngredient, ListIngredients,
                          IncludeIngredientInPalette, ExcludeIngredientInPalette, RemoveIngredientFromPalette ]:
            q = queue.Queue()
            f = Function( call_q = q, message_q = self.message_q, session = self.session )
            self.mapper.register_function( f )
        
    def power_on( self ):
        self._log.info( 'powering on' )
        
        self.listener.start()
        self.emitter.start()
        self.mapper.start()
