from ._function import Function

from hooke.model import ConceptPalette

class CreateSeed( Function ):

    @property
    def name( self ):
        return 'create_seed'
    
    @property
    def command_rx( self ):
        return r"^create seed \"(?P<title>.*?)\" from (?P<cid>\w+) and (?P<pid>\w+), \"(?P<notes>.*?)\"$"

    def _process_call( self, call, session ):
        cp = ConceptPalette( concept_id = call['cid'], palette_id = call['pid'], 
                             title = call['title'], notes = call['notes'] )
        
        session.add( cp )
        session.commit()
        return '*&lt;success&gt;* created seed *%s|%s*\n' % ( call['cid'], call['pid'] )
