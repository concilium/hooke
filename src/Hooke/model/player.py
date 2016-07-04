from sqlalchemy import Column, String

from . import HookeModelBase

class Player( HookeModelBase ):
    __tablename__ = 'player'

    # attributes
        
    id = Column( 'id', String, primary_key = True )
    password = Column( 'password', String, nullable = False  )
    first_name = Column( 'first_name', String, nullable = False  )
    last_name = Column( 'last_name', String, nullable = False  )
    email = Column( 'email', String, nullable = False  )
    
    # relationships
    
    # miscellaneous
    
    def __repr__( self ):
        return ( "<Player[%s]>" % ( self.id ) )
