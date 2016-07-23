import logging
import threading
import time
import random

from slackclient import SlackClient

class Listener( threading.Thread ):

    def __init__( self, slack_bot_token, slack_bot_name, slack_channel_name, command_q ):
        self._log = logging.getLogger( 'hooke.bot.Listener' )
        self._log.info( 'listener initializing' )
        
        threading.Thread.__init__( self )
        
        self.slack_bot_token = slack_bot_token
        self.slack_client = SlackClient( self.slack_bot_token )

        self._log.debug( 'mapping bot name "%s" -> slack_bot_id', slack_bot_name )
        self.slack_bot_name = slack_bot_name
        sac = self.slack_client.api_call( 'users.list' )
        if sac.get( 'ok' ):
            users = sac.get( 'members' )
            for u in users:
                if 'name' in u and u.get( 'name' ) == slack_bot_name:
                    self.slack_bot_id = u.get( 'id' )
                    self._log.debug( 'set slack_bot_id = %s', self.slack_bot_id )

        self._log.debug( 'mapping channel name "%s" -> slack_channel_id', slack_channel_name )
        self.slack_channel_name = slack_channel_name
        sac = self.slack_client.api_call( 'channels.list' )
        if sac.get( 'ok' ):
            channels = sac.get( 'channels' )
            for c in channels:
                if 'name' in c and c.get( 'name' ) == slack_channel_name:
                    self.slack_channel_id = c.get( 'id' )
                    self._log.debug( 'set slack_channel_id = %s', self.slack_channel_id )

        self.at_marker = '<@' + self.slack_bot_id + '>:'
        self._log.debug( 'using marker "%s"', self.at_marker )
        
        self.command_q = command_q

    def run( self ):
        self._log.info( 'listener starting' )
        
        if self.slack_client.rtm_connect():
            self._log.debug( 'connected to slack, entering loop' )
            while True:
                output = self.slack_client.rtm_read()
                if output and len( output ) > 0:
                    for o in output:
                        if o and 'text' in o and self.at_marker in o['text']:
                            command = o['text'].split( self.at_marker )[1].strip()
                            
                            self._log.debug( 'enqueuing command: %s', command )
                            self.command_q.put( command )

                time.sleep( 0.5 + random.random() )
