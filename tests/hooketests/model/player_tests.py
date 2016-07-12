from unittest import TestCase
from nose.plugins.attrib import attr

import hooke

from ._attributes import player_attribs
from ._helpers import check_attr, compare_attrs, check_repr

class PlayerTests( TestCase ):

    @attr( type = 'existence' )
    def test_player_model( self ):
        '''verify existence and attributes of "Player" model class'''
    
        check_attr( hooke.model, 'Player' )
        
        p = hooke.model.Player( **player_attribs )
        compare_attrs( p, player_attribs )
        check_repr( p, p.id )
    
    @attr( type = 'persistence' )
    def test_player_persistence( self ):
        '''verify persistence of "Player" instances'''
        
        ses1 = hooke.model.SQLiteMemorySession()
        p1 = hooke.model.Player( **player_attribs )
        ses1.add( p1 )
        ses1.commit()
        ses1.close()
    
        ses2 = hooke.model.SQLiteMemorySession()
        p2 = ses2.query( hooke.model.Player ).filter( hooke.model.Player.id == player_attribs['id'] ).one()
        compare_attrs( p2, player_attribs )
        ses2.delete( p2 )
        ses2.commit()
        ses2.close()
