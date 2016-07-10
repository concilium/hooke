from enum import Enum

class Flavor( Enum ):
    include = 'include'
    exclude = 'exclude'

class State( Enum ):
    active = 'active'
    inactive = 'inactive'

class Position( Enum ):
    initial = 'initial'
    medial = 'medial'
    final = 'final'

class Tone( Enum ):
    light = 'light'
    dark = 'dark'
