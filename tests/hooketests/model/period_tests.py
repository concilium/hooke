from unittest import TestCase
from nose.plugins.attrib import attr

import hooke

from ._factory import period_attribs, add_period, query_period, delete_period
from ._factory import initial_period_attribs, add_initial_period, query_initial_period, delete_initial_period
from ._factory import medial_period_attribs, add_medial_period, query_medial_period, delete_medial_period
from ._factory import final_period_attribs, add_final_period, query_final_period, delete_final_period
from ._helpers import check_attr, compare_attrs, check_repr, SQLiteMemorySession

class PeriodTests( TestCase ):

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and attributes of "Period" model class'''
    
        check_attr( hooke.model, 'Period' )
        
        p = hooke.model.Period( **period_attribs )
        compare_attrs( p, period_attribs )
        check_repr( p, p.id )
    
    @attr( type = 'persistence' )
    def test_persistence( self ):
        '''verify persistence of "Period" instances'''
        
        ses1 = SQLiteMemorySession()
        add_period( ses1 )
        ses1.commit()
        ses1.close()
    
        ses2 = SQLiteMemorySession()
        p = query_period( ses2 )
        compare_attrs( p, period_attribs )
        delete_period( ses2 )
        ses2.commit()
        ses2.close()

class InitialPeriodTests( TestCase ):

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and attributes of "InitialPeriod" model class'''
    
        check_attr( hooke.model, 'InitialPeriod' )
        
        p = hooke.model.InitialPeriod( **initial_period_attribs )
        compare_attrs( p, initial_period_attribs )
        check_repr( p, p.id )

class MedialPeriodTests( TestCase ):

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and attributes of "MedialPeriod" model class'''
    
        check_attr( hooke.model, 'MedialPeriod' )
        
        p = hooke.model.MedialPeriod( **medial_period_attribs )
        compare_attrs( p, medial_period_attribs )
        check_repr( p, p.id )

class FinalPeriodTests( TestCase ):

    @attr( type = 'existence' )
    def test_existence( self ):
        '''verify existence and attributes of "FinalPeriod" model class'''
    
        check_attr( hooke.model, 'FinalPeriod' )
        
        p = hooke.model.FinalPeriod( **final_period_attribs )
        compare_attrs( p, final_period_attribs )
        check_repr( p, p.id )

class PeriodSequenceTests( TestCase ):

    @attr( type = 'persistence' )
    def test_persistence( self ):
        '''verify persistence of chain of "[Initial|Medial|Final]Period" instances'''
        
        ses1 = SQLiteMemorySession()
        add_initial_period( ses1, composed = True )
        add_medial_period( ses1 )
        add_final_period( ses1 )
        ses1.commit()
        ses1.close()
    
        ses2 = SQLiteMemorySession()
        ip = query_initial_period( ses2 )
        compare_attrs( ip, initial_period_attribs )
        mp = query_medial_period( ses2 )
        compare_attrs( mp, medial_period_attribs )
        fp = query_final_period( ses2 )
        compare_attrs( fp, final_period_attribs )
        delete_final_period( ses2 )
        delete_medial_period( ses2 )
        delete_initial_period( ses2, composed = True )
        ses2.commit()
        ses2.close()
