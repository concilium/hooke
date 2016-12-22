from datetime import datetime

from ._function import Function

from hooke.model import History, State, InitialPeriod, FinalPeriod, Tone

class StartHistory( Function ):

    @property
    def name( self ):
        return 'start_history'
    
    @property
    def command_rx( self ):
        return ( r"^" +
                 r"start history \"(?P<title>.*?)\" as (?P<hid>\w+), using (?P<cid>\w+)\|(?P<pid>\w+), with " +
                 r"initial (?P<iptone>light|dark) period (?P<ipid>\w+) \"(?P<ipdescription>.*?)\" and " +
                 r"final (?P<fptone>light|dark) period (?P<fpid>\w+) \"(?P<fpdescription>.*?)\"" + 
                 r"$" )

    def _process_call( self, call, session ):

        h = History ( id = call['hid'],
                      title = call['title'],
                      concept_id = call['cid'],
                      palette_id = call['pid'],
                      started_on = datetime.now(),
                      state = State.active )
        session.add( h )
        session.commit()

        ip = InitialPeriod( id = call['ipid'],
                            history_id = call['hid'],
                            description = call['ipdescription'],
                            tone = Tone[call['iptone']],
                            next_period_id = call['fpid'] )
        session.add( ip )

        fp = FinalPeriod( id = call['fpid'],
                          history_id = call['hid'],
                          description = call['fpdescription'],
                          tone = Tone[call['fptone']],
                          prev_period_id = call['ipid'] )
        session.add( fp )
        
        session.commit()
        
        return '*&lt;success&gt;* started history *%s*\n' % ( call['hid'] )
