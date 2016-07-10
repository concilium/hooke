from nose.plugins.attrib import attr

import Hooke

from ._attributes import concept_attribs, palette_attribs, concept_palette_attribs, history_attribs, player_attribs, history_player_attribs
from ._helpers import check_attr, compare_attrs, check_assoc_repr

class HistoryPlayerTests:

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and attributes of "HistoryPlayer" model class'''
    
        check_attr( Hooke.model, 'HistoryPlayer' )
        
        hp = Hooke.model.HistoryPlayer( **history_player_attribs )
        compare_attrs( hp, history_player_attribs )
        check_assoc_repr( hp, hp.history_id, hp.player_id )

    @attr( type = 'persistence' )
    def test_persistence( self ):
        '''verify persistence of "HistoryPlayer" instances'''
        
        ses1 = Hooke.model.SQLiteMemorySession()
        c1 = Hooke.model.Concept( **concept_attribs )
        ses1.add( c1 )
        pal1 = Hooke.model.Palette( **palette_attribs )
        ses1.add( pal1 )
        cp1 = Hooke.model.ConceptPalette( **concept_palette_attribs )
        ses1.add( cp1 )
        h1 = Hooke.model.History( **history_attribs )
        ses1.add( h1 )
        play1 = Hooke.model.Player( **player_attribs )
        ses1.add( play1 )
        hp1 = Hooke.model.HistoryPlayer( **history_player_attribs )
        ses1.add( hp1 )
        ses1.commit()
        ses1.close()
    
        ses2 = Hooke.model.SQLiteMemorySession()
        hp2 = ses2.query( Hooke.model.HistoryPlayer ).filter(
                                Hooke.model.HistoryPlayer.history_id == history_player_attribs['history_id'],
                                Hooke.model.HistoryPlayer.player_id == history_player_attribs['player_id']
        ).one()
        compare_attrs( hp2, history_player_attribs )
        ses2.delete( hp2 )
        play2 = ses2.query( Hooke.model.Player ).filter( Hooke.model.Player.id == player_attribs['id'] ).one()
        ses2.delete( play2 )
        h2 = ses2.query( Hooke.model.History ).filter( Hooke.model.History.id == history_attribs['id'] ).one()
        ses2.delete( h2 )
        cp2 = ses2.query( Hooke.model.ConceptPalette ).filter(
                            Hooke.model.ConceptPalette.concept_id == concept_palette_attribs['concept_id'],
                            Hooke.model.ConceptPalette.palette_id == concept_palette_attribs['palette_id']
        ).one()
        ses2.delete( cp2 )
        pal2 = ses2.query( Hooke.model.Palette ).filter( Hooke.model.Palette.id == palette_attribs['id'] ).one()
        ses2.delete( pal2 )
        c2 = ses2.query( Hooke.model.Concept ).filter( Hooke.model.Concept.id == concept_attribs['id'] ).one()
        ses2.delete( c2 )
        ses2.commit()
        ses2.close()
    
    @attr( type = 'association' )
    def test_associations( self ):
        '''verify behavior of history-to-player association'''
        
        ses = Hooke.model.SQLiteMemorySession()
        c = Hooke.model.Concept( **concept_attribs )
        ses.add( c )
        pal = Hooke.model.Palette( **palette_attribs )
        ses.add( pal )
        cp = Hooke.model.ConceptPalette( **concept_palette_attribs )
        ses.add( cp )
        h = Hooke.model.History( **history_attribs )
        ses.add( h )
        play = Hooke.model.Player( **player_attribs )
        ses.add( play )
        hp = Hooke.model.HistoryPlayer( **history_player_attribs )
        ses.add( hp )
        ses.commit()
        
        assert len( h.history_players ) == 1
        assert h.history_players[0] == hp
        assert len( h.players ) == 1
        assert h.players[0] == play
    
        assert len( play.history_players ) == 1
        assert play.history_players[0] == hp
        assert len( play.histories ) == 1
        assert play.histories[0] == h
    
        ses.delete( hp )
        ses.delete( play )
        ses.delete( h )
        ses.delete( cp )
        ses.delete( pal )
        ses.delete( c )
        ses.commit()
        ses.close()
