from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from hooke.model import HookeModelBase

def check_attr( thing, attribute ):
    assert hasattr( thing, attribute ), '%s has no "%s" attribute' % ( thing, attribute )

def compare_attrs( thing, attributes ):
    for a in attributes.keys():
        expected = attributes[a]
        found = getattr( thing, a )
        assert ( expected == found ), 'expected attribute "%s" of %s to be "%s", found "%s"' % ( a, thing, expected, found )

def check_repr( thing, pkey ):
    expected = '<%s[%s]>' % ( type( thing ).__name__, pkey )
    found = thing.__repr__()
    assert ( expected == found ), 'expected representation "%s", found "%s"' % ( expected, found )

def check_assoc_repr( thing, left_pkey, right_pkey ):
    expected = '<%s[%s,%s]>' % ( type( thing ).__name__, left_pkey, right_pkey )
    found = thing.__repr__()
    assert ( expected == found ), 'expected representation "%s", found "%s"' % ( expected, found )

engine = create_engine( 'sqlite://' )
HookeModelBase.metadata.create_all( engine )
SQLiteMemorySession = sessionmaker( engine )
