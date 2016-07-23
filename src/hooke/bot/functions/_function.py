from abc import ABC, abstractmethod

import logging
import threading

class Function( ABC, threading.Thread ):
    
    def __init__( self, call_q, message_q, session ):
        self._log = logging.getLogger( 'hooke.bot.functions.' + self.__class__.__name__ )
        self._log.info( '%s initializing', self.name )
        
        threading.Thread.__init__( self )

        self.call_q = call_q
        self.message_q = message_q
        self.session = session
        
    @property
    @abstractmethod
    def name( self ):
        pass

    @property
    @abstractmethod
    def command_rx( self ):
        pass

    @abstractmethod
    def _process_call( self, call, session ):
        pass

    def run( self ):
        self._log.info( '%s starting', self.name )

        while True:
            call = self.call_q.get()
            self._log.debug( 'dequeued call: %s', call )

            message = '*&lt;error&gt;* problem processing %s call, check logs for more information\n' % ( self.name )
            try:
                message = self._process_call( call, self.session )
            except:
                self.session.rollback()
                self._log.warning( 'caught exception', exc_info = True )
            finally:
                self.session.close()
                self.session.remove()

            self._log.debug( 'enqueuing message: %s', message )
            self.message_q.put( message )
