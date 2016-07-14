from unittest import TestCase
from nose.plugins.attrib import attr

import hooke

from ._factory import history_player_attribs, add_history_player, query_history_player, delete_history_player, query_history, query_player
from ._helpers import check_attr, compare_attrs, check_assoc_repr

class HistoryPlayerTests( TestCase ):

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and attributes of "HistoryPlayer" model class'''
    
        check_attr( hooke.model, 'HistoryPlayer' )
        
        hp = hooke.model.HistoryPlayer( **history_player_attribs )
        compare_attrs( hp, history_player_attribs )
        check_assoc_repr( hp, hp.history_id, hp.player_id )

    @attr( type = 'persistence' )
    def test_persistence( self ):
        '''verify persistence of "HistoryPlayer" instances'''
        
        ses1 = hooke.model.SQLiteMemorySession()
        add_history_player( ses1 )
        ses1.commit()
        ses1.close()

        ses2 = hooke.model.SQLiteMemorySession()
        hp = query_history_player( ses2 )
        compare_attrs( hp, history_player_attribs )
        delete_history_player( ses2 )
        ses2.commit()
        ses2.close()

    @attr( type = 'association' )
    def test_associations( self ):
        '''verify behavior of history-to-player association'''

        ses = hooke.model.SQLiteMemorySession()
        add_history_player( ses )
        ses.commit()

        h = query_history( ses )
        p = query_player( ses )
        hp = query_history_player( ses )
        
        assert len( h.history_players ) == 1
        assert h.history_players[0] == hp
        assert len( h.players ) == 1
        assert h.players[0] == p
    
        assert len( p.history_players ) == 1
        assert p.history_players[0] == hp
        assert len( p.histories ) == 1
        assert p.histories[0] == p

        delete_history_player( ses )
        ses.commit()
        ses.close()
