import re

from pydispatch import dispatcher

echo_signal = 'echo'
echo_pattern = re.compile( r"^echo (?P<message>.*)$" )

def echo_handler( sender, factory, client, channel, match ):
    
    message = match.group( 'message' )
    
    print( 'dispatching on post_message' )
    dispatcher.send( signal = 'post_message',
                     sender = 'echo_handler',
                     client = client,
                     channel = channel,
                     message = message )
        
dispatcher.connect( echo_handler, 
                    signal = echo_signal,
                    sender = dispatcher.Any )
