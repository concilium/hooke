import datetime
import nose

import Hooke

def test_model():
    '''verify existence of "model" package in Hooke module'''
    _check_attr( Hooke, 'model' )
