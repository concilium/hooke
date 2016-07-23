import logging
import re
import threading

class EchoFunction( threading.Thread ):
    
    function_name = 'echo'
    command_pattern = re.compile( r"^echo (?P<text>.*)$" )    

    def __init__( self, call_q, message_q, session ):
        self._log = logging.getLogger( 'hooke.bot.EchoFunction' )
        self._log.info( 'echo_function initializing' )
        
        threading.Thread.__init__( self )

        self.call_q = call_q
        self.message_q = message_q
        self.session = session
        
    def run( self ):
        self._log.info( 'echo_function starting' )

        while True:
            call = self.call_q.get()
            self._log.debug( 'dequeued call: %s', call )
            
            message = call['text']
            
            self._log.debug( 'enqueuing message: %s', message )
            self.message_q.put( message )
