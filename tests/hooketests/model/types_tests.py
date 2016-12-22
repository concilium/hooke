from unittest import TestCase
from nose.plugins.attrib import attr

import hooke

from ._helpers import check_attr

class FlavorTests( TestCase ):
    
    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and values of "Flavor" enumeration'''
    
        check_attr( hooke.model, 'Flavor' )
        assert hooke.model.Flavor.include
        assert hooke.model.Flavor.exclude

class StateTests( TestCase ):

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and values of "State" enumeration'''
    
        check_attr( hooke.model, 'State' )
        assert hooke.model.State.active
        assert hooke.model.State.inactive

class PlacementTests( TestCase ):

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and values of "Placement" enumeration'''
    
        check_attr( hooke.model, 'Placement' )
        assert hooke.model.Placement.detached
        assert hooke.model.Placement.initial
        assert hooke.model.Placement.medial
        assert hooke.model.Placement.final

class ToneTests( TestCase ):

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and values of "Tone" enumeration'''
    
        check_attr( hooke.model, 'Tone' )
        assert hooke.model.Tone.light
        assert hooke.model.Tone.dark
