import logging
import re
import threading

from hooke.model import Concept

class MakeConceptFunction( threading.Thread ):
    
    function_name = 'make_concept'
    command_pattern = re.compile( r"^make concept \"(?P<description>.*?)\" as (?P<id>\w+)$" )    

    def __init__( self, call_q, message_q, session ):
        self._log = logging.getLogger( 'hooke.bot.MakeConceptFunction' )
        self._log.info( 'make_concept_function initializing' )
        
        threading.Thread.__init__( self )

        self.call_q = call_q
        self.message_q = message_q
        self.session = session
        
    def run( self ):
        self._log.info( 'make_concept_function starting' )

        while True:
            call = self.call_q.get()
            self._log.debug( 'dequeued call: %s', call )

            message = '*&lt;error&gt;* unable to make concept\n'
            c = Concept( id = call['id'], description = call['description'] )
            try:
                self.session.add( c )
                self.session.commit()
                message = '*&lt;success&gt;* made concept *%s*\n' % ( call['id'] )
            except:
                self.session.rollback()
                self._log.warning( 'problem making concept', exc_info = True )
            finally:
                self.session.close()
                self.session.remove()

            self._log.debug( 'enqueuing message: %s', message )
            self.message_q.put( message )

class ListConceptsFunction( threading.Thread ):
    
    function_name = 'list_concepts'
    command_pattern = re.compile( r"^list concepts$" )

    def __init__( self, call_q, message_q, session ):
        self._log = logging.getLogger( 'hooke.bot.ListConceptsFunction' )
        self._log.info( 'list_concepts_function initializing' )
        
        threading.Thread.__init__( self )

        self.call_q = call_q
        self.message_q = message_q
        self.session = session
        
    def run( self ):
        self._log.info( 'list_concepts_function starting' )

        while True:
            call = self.call_q.get()
            self._log.debug( 'dequeued call: %s', call )

            message = '*&lt;error&gt;* unable to list concepts\n'
            try:
                cs = self.session.query( Concept ).all()
                if len( cs ) > 0:
                    message = '*&lt;success&gt;* listing concepts:\n'
                    for c in cs:
                        message += ( '<%s> %s\n' % ( c.id, c.description ) )
            except:
                self.session.rollback()
                self._log.warning( 'problem listing concepts', exc_info = True )
            finally:
                self.session.close()
                self.session.remove()

            self._log.debug( 'enqueuing message: %s', message )
            self.message_q.put( message )

class DropConceptFunction( threading.Thread ):
    
    function_name = 'drop_concept'
    command_pattern = re.compile( r"^drop concept (?P<id>\w+)$" )

    def __init__( self, call_q, message_q, session ):
        self._log = logging.getLogger( 'hooke.bot.DropConceptFunction' )
        self._log.info( 'drop_concept_function initializing' )
        
        threading.Thread.__init__( self )

        self.call_q = call_q
        self.message_q = message_q
        self.session = session
        
    def run( self ):
        self._log.info( 'drop_concept_function starting' )

        while True:
            call = self.call_q.get()
            self._log.debug( 'dequeued call: %s', call )

            message = '*&lt;error&gt;* unable to drop concept\n'
            try:
                c = self.session.query( Concept ).filter( Concept.id == call['id'] ).one()
                self.session.delete( c )
                self.session.commit()
                message = '*&lt;success&gt;* dropped concept *%s*\n' % ( call['id'] )
            except:
                self.session.rollback()
                self._log.warning( 'problem dropping concept', exc_info = True )
            finally:
                self.session.close()
                self.session.remove()

            self._log.debug( 'enqueuing message: %s', message )
            self.message_q.put( message )
