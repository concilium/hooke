from sqlalchemy import Column, String, ForeignKey
from sqlalchemy_enum34 import EnumType

from . import HookeModelBase, Placement, Tone

class Period( HookeModelBase ):
    __tablename__ = 'period'

    # attributes
        
    id = Column( 'id', String, primary_key = True )
    history_id = Column( 'history_id', String, ForeignKey( 'history.id' ), nullable = False )
    placement = Column( 'placement', EnumType( Placement, name = 'placement' ), nullable = False )
    description = Column( 'description', String, nullable = False )
    tone = Column( 'tone', EnumType( Tone, name = 'tone' ), nullable = False )

    # relationships

    # subclassing
    
    __mapper_args__ = {
        'polymorphic_on'       : placement,
        'polymorphic_identity' : Placement.detached,
    }
        
    # miscellaneous
    
    def __repr__( self ):
        return ( "<Period[%s]>" % ( self.id ) )

class InitialPeriod( Period ):
    __tablename__ = 'initialperiod'

    # attributes
        
    id = Column( 'id', String, ForeignKey( 'period.id' ), primary_key = True )
    next_period_id = Column( 'next_period_id', String, ForeignKey( 'period.id' ), nullable = False )

    # relationships

    # subclassing
    
    __mapper_args__ = {
        'polymorphic_identity' : Placement.initial,
        'inherit_condition'    : id == Period.id,
    }
        
    # miscellaneous
    
    def __repr__( self ):
        return ( "<InitialPeriod[%s]>" % ( self.id ) )

class MedialPeriod( Period ):
    __tablename__ = 'medialperiod'
 
    # attributes
         
    id = Column( 'id', String, ForeignKey( 'period.id' ), primary_key = True )
    prev_period_id = Column( 'prev_period_id', String, ForeignKey( 'period.id' ), nullable = False )
    next_period_id = Column( 'next_period_id', String, ForeignKey( 'period.id' ), nullable = False )
 
    # relationships
 
    # subclassing
     
    __mapper_args__ = {
        'polymorphic_identity' : Placement.medial,
        'inherit_condition'    : id == Period.id,
    }
         
    # miscellaneous
     
    def __repr__( self ):
        return ( "<MedialPeriod[%s]>" % ( self.id ) )
 
class FinalPeriod( Period ):
    __tablename__ = 'finalperiod'
 
    # attributes
         
    id = Column( 'id', String, ForeignKey( 'period.id' ), primary_key = True )
    prev_period_id = Column( 'prev_period_id', String, ForeignKey( 'period.id' ), nullable = False )

    # relationships
 
    # subclassing
     
    __mapper_args__ = {
        'polymorphic_identity' : Placement.final,
        'inherit_condition'    : id == Period.id,
    }
         
    # miscellaneous
     
    def __repr__( self ):
        return ( "<FinalPeriod[%s]>" % ( self.id ) )
