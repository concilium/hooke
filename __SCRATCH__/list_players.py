import re

from pydispatch import dispatcher
from hooke.model import session_scope, Player

list_players_signal = 'list_players'
list_players_pattern = re.compile( r"^list players$" )

def list_players_handler( sender, factory, client, channel, match ):
        
    message = 'Listing players:\n'
    with session_scope( factory ) as ses:
        players = ses.query( Player ).all()
        for p in players:
            message += ( p.__repr__() + '\n' )
    
    print( 'dispatching on post_message' )
    dispatcher.send( signal = 'post_message',
                     sender = 'list_players_handler',
                     client = client,
                     channel = channel,
                     message = message )
    
dispatcher.connect( list_players_handler, 
                    signal = list_players_signal,
                    sender = dispatcher.Any )
