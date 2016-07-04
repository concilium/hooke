from enum import Enum

class Flavor( Enum ):
    include = 'include'
    exclude = 'exclude'

class Tone( Enum ):
    light = 'light'
    dark = 'dark'

class State( Enum ):
    active = 'active'
    inactive = 'inactive'
