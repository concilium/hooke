from nose.plugins.attrib import attr

import Hooke

from HookeTests.model_tests import period_attribs
from HookeTests.model_tests import check_attr, compare_attrs, check_repr

class PeriodTests:
    
    @attr( type = 'existence' )
    def test_period_model( self ):
        '''verify existence and attributes of "Period" model class'''
    
        check_attr( Hooke.model, 'Period' )
        
        p = Hooke.model.Period( **period_attribs )
        compare_attrs( p, period_attribs )
        check_repr( p, p.id )

    @attr( type = 'persistence' )
    def test_period_persistence( self ):
        '''verify persistence of "Period" instances'''
        
        ses1 = Hooke.model.SQLiteMemorySession()
        p1 = Hooke.model.Period( **period_attribs )
        ses1.add( p1 )
        ses1.commit()
        ses1.close()
    
        ses2 = Hooke.model.SQLiteMemorySession()
        p2 = ses2.query( Hooke.model.Period ).filter( Hooke.model.Period.id == period_attribs['id'] ).one()
        compare_attrs( p2, period_attribs )
        ses2.delete( p2 )
        ses2.commit()
        ses2.close()
