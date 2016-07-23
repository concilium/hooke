import re

from pydispatch import dispatcher
from hooke.model import session_scope, Player

add_player_signal = 'add_player'
add_player_pattern = re.compile( r"^add player (?P<id>\w+) with first_name (?P<fname>.*?), last_name (?P<lname>.*?), email (?P<email>.*?)$" )

def add_player_handler( sender, factory, client, channel, match ):

    pid = match.group( 'id' )
    fname = match.group( 'fname' )
    lname = match.group( 'lname' )
    email = match.group( 'email' )

    with session_scope( factory ) as ses:
        p = Player( id = pid, fname = fname, lname = lname, email = email )
        ses.add( p )

    print( 'dispatching on post_message' )
    dispatcher.send( signal = 'post_message',
                     sender = 'add_player_handler',
                     client = client,
                     channel = channel,
                     message = 'added ' + p.__repr__() )
    
dispatcher.connect( add_player_handler, 
                    signal = add_player_signal,
                    sender = dispatcher.Any )
