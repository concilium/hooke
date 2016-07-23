import random
import threading
import time
import re

from slackclient import SlackClient
from pydispatch import dispatcher

from .wiring import Senders, Signals

class Relay( threading.Thread ):
    
    def __init__( self, slack_bot_token, slack_bot_name, slack_channel_name ):
        threading.Thread.__init__( self )

        self.slack_bot_token = slack_bot_token
        self.slack_client = SlackClient( self.slack_bot_token )

        self.slack_bot_name = slack_bot_name
        sac = self.slack_client.api_call( 'users.list' )
        if sac.get( 'ok' ):
            users = sac.get( 'members' )
            for u in users:
                if 'name' in u and u.get( 'name' ) == slack_bot_name:
                    self.slack_bot_id = u.get( 'id' )
                    print( 'set slack_bot_id = %s' % self.slack_bot_id )   #DEBUG

        self.slack_channel_name = slack_channel_name
        sac = self.slack_client.api_call( 'channels.list' )
        if sac.get( 'ok' ):
            channels = sac.get( 'channels' )
            for c in channels:
                if 'name' in c and c.get( 'name' ) == slack_channel_name:
                    self.slack_channel_id = c.get( 'id' )
                    print( 'set slack_channel_id = %s' % self.slack_channel_id )    #DEBUG

        self.at_marker = '<@' + self.slack_bot_id + '>:'

        self.sender_name = Senders.RELAY
        self.dispatch_table = {
            Signals.ECHO                           : re.compile( r"^echo (?P<message>.*)$" ),
            Signals.MAKE_CONCEPT                   : re.compile( r"^make concept \"(?P<description>.*?)\" as (?P<cid>\w+)$" ),
            Signals.LIST_CONCEPTS                  : re.compile( r"^list concepts$" ),
            Signals.MAKE_PALETTE                   : re.compile( r"^make palette \"(?P<description>.*?)\" as (?P<pid>\w+)$" ),
            Signals.LIST_PALETTES                  : re.compile( r"^list palettes$" ),
            Signals.MAKE_INGREDIENT                : re.compile( r"^make ingredient \"(?P<description>.*?)\" as (?P<iid>\w+)$" ),
            Signals.LIST_INGREDIENTS               : re.compile( r"^list ingredients$" ),
            Signals.INCLUDE_INGREDIENT_IN_PALETTE  : re.compile( r"^include ingredient (?P<iid>\w+) in (?P<pid>\w+)$" ),
            Signals.EXCLUDE_INGREDIENT_IN_PALETTE  : re.compile( r"^exclude ingredient (?P<iid>\w+) in (?P<pid>\w+)$" ),
            Signals.REMOVE_INGREDIENT_FROM_PALETTE : re.compile( r"^remove ingredient (?P<iid>\w+) from (?P<pid>\w+)$" ),
            Signals.CREATE_SEED                    : re.compile( r"^create seed \"(?P<title>.*?)\" from (?P<cid>\w+) and (?P<pid>\w+), \"(?P<notes>.*?)\"$" ),
            Signals.LIST_SEEDS                     : re.compile( r"^list seeds$" ),
            Signals.SHOW_SEED                      : re.compile( r"^show seed (?P<cid>\w+)\|(?P<pid>\w+)$"),
            Signals.MAKE_PLAYER                    : re.compile( r"^make player (?P<fname>\w+) (?P<lname>\w+) &lt;(?P<email>.*?)&gt; as (?P<pid>\w+)$" ),
            Signals.START_HISTORY                  : re.compile( r"^start history \"(?P<title>.*?)\" as (?P<hid>\w+), using (?P<cid>\w+) and (?P<pid>\w+)$" ),
            Signals.LIST_HISTORIES                 : re.compile( r"^list histories$" ),
            Signals.SHOW_HISTORY                   : re.compile( r"^show history (?P<hid>\w+)$" ),
            Signals.LIST_PLAYERS                   : re.compile( r"^list players$" ),
        }
        dispatcher.connect( self.post_message_handler, Signals.POST_MESSAGE, dispatcher.Any )
        
    def post_message_handler( self, message ):

        print( 'posting message' )  #DEBUG
        self.slack_client.api_call( 'chat.postMessage', 
                                    channel = self.slack_channel_id, 
                                    text = message,
                                    as_user = True )

    def run( self ):
        
        if self.slack_client.rtm_connect():
            print( 'relay connected, entering loop' )   #DEBUG
            while True:
                output = self.slack_client.rtm_read()
                if output and len( output ) > 0:
                    for o in output:
                        if o and 'text' in o and self.at_marker in o['text']:

                            command = o['text'].split( self.at_marker )[1].strip()

                            print( 'trying to match command = %s' % ( command ) )   #DEBUG

                            matched = False
                            for signal, pattern in self.dispatch_table.items():
                                match = pattern.match( command )
                                if match:
                                    matched = True
                                    print( 'dispatching on %s' % ( signal ) )       #DEBUG
                                    dispatcher.send( signal = signal,
                                                     sender = self.sender_name,
                                                     **match.groupdict() )
                            if not matched:
                                dispatcher.send( signal = Signals.POST_MESSAGE,
                                                 sender = self.sender_name,
                                                 message = "(unrecognized command)\n" )
                                
                time.sleep( 0.5 + random.random() )
