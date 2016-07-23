import logging
import queue

from sqlalchemy.orm import scoped_session, sessionmaker

from .listener import Listener
from .emitter import Emitter
from .mapper import Mapper
from .echo_function import EchoFunction
from .concept_functions import MakeConceptFunction, ListConceptsFunction, DropConceptFunction

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

        self.echo_call_q = queue.Queue()
        echo_f = EchoFunction( call_q = self.echo_call_q,
                               message_q = self.message_q,
                               session = self.session )
        self.mapper.register_function( echo_f )

        self.make_concept_call_q = queue.Queue()
        make_concept_f = MakeConceptFunction( call_q = self.make_concept_call_q,
                                              message_q = self.message_q,
                                              session = self.session )
        self.mapper.register_function( make_concept_f )

        self.list_concepts_call_q = queue.Queue()
        list_concepts_f = ListConceptsFunction( call_q = self.list_concepts_call_q,
                                                message_q = self.message_q,
                                                session = self.session )
        self.mapper.register_function( list_concepts_f )
        
        self.drop_concept_call_q = queue.Queue()
        drop_concept_f = DropConceptFunction( call_q = self.drop_concept_call_q,
                                              message_q = self.message_q,
                                              session = self.session )
        self.mapper.register_function( drop_concept_f )


    def power_on( self ):
        self._log.info( 'powering on' )
        
        self.listener.start()
        self.emitter.start()
        self.mapper.start()
