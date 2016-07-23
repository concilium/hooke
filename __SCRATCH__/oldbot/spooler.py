from pydispatch import dispatcher
from .wiring import Senders, Signals

class Spooler:

    def __init__( self ):
        
        self.sender_name = Senders.SPOOLER
    
    def spool( self ):
        
        print( 'spooling ...' )     #DEBUG

        print( '+ making concept: interregnum' )        #DEBUG
        dispatcher.send( signal = Signals.MAKE_CONCEPT,
                         sender = self.sender_name,
                         cid = 'interregnum',
                         description = 'A brutal interregnum follows the unexpected death of a leader.'
        )

        print( '... completed spool.' )     #DEBUG
