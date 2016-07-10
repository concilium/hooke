from nose.plugins.attrib import attr

import Hooke

from ._helpers import check_attr

class FlavorTests:
    
    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and values of "Flavor" enumeration'''
    
        check_attr( Hooke.model, 'Flavor' )
        assert Hooke.model.Flavor.include
        assert Hooke.model.Flavor.exclude

class StateTests:

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and values of "State" enumeration'''
    
        check_attr( Hooke.model, 'State' )
        assert Hooke.model.State.active
        assert Hooke.model.State.inactive

class PositionTests:

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and values of "Position" enumeration'''
    
        check_attr( Hooke.model, 'Position' )
        assert Hooke.model.Position.initial
        assert Hooke.model.Position.medial
        assert Hooke.model.Position.final

class ToneTests:

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and values of "Tone" enumeration'''
    
        check_attr( Hooke.model, 'Tone' )
        assert Hooke.model.Tone.light
        assert Hooke.model.Tone.dark
