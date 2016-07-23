import logging
import re
import threading

class Mapper( threading.Thread ):

    def __init__( self, command_q ):
        self._log = logging.getLogger( 'hooke.bot.Mapper' )
        self._log.info( 'mapper initializing' )
        
        threading.Thread.__init__( self )
        
        self.command_q = command_q
        self.functions = []

    def register_function( self, function ):
        self._log.info( 'registering %s function', function.name )

        self.functions.append( function )

    def run( self ):
        self._log.info( 'mapper starting' )

        f_map = []
        for f in self.functions:
            f_map.append( {
                'name'  : f.name,
                'rx'    : re.compile( f.command_rx ),
                'callq' : f.call_q,
            } )
            f.start()

        while True:
            command = self.command_q.get()
            self._log.debug( 'dequeued command: %s', command )
            
            matched = False
            for f in f_map:
                match = f['rx'].match( command )
                if match:
                    matched = True
                    call = match.groupdict()
                    
                    self._log.debug( 'enqueuing %s call: %s', f['name'], call )
                    f['callq'].put( call )
                    
            if not matched:
                self._log.warning( 'unrecognized command, ignoring' )
