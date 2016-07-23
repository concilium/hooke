import logging
import threading

class Mapper( threading.Thread ):

    def __init__( self, command_q ):
        self._log = logging.getLogger( 'hooke.bot.Mapper' )
        self._log.info( 'mapper initializing' )
        
        threading.Thread.__init__( self )
        
        self.command_q = command_q
        self.functions = []

    def register_function( self, function ):
        self._log.info( 'registering %s function', function.function_name )
        self.functions.append( function )

    def run( self ):
        self._log.info( 'mapper starting' )

        for f in self.functions:
            f.start()

        while True:
            command = self.command_q.get()
            self._log.debug( 'dequeued command: %s', command )
            
            matched = False
            for f in self.functions:
                match = f.command_pattern.match( command )
                if match:
                    matched = True
                    call = match.groupdict()
                    
                    self._log.debug( 'enqueuing %s call: %s', f.function_name, call )
                    f.call_q.put( call )
                    
            if not matched:
                self._log.warning( 'unrecognized command, ignoring' )
