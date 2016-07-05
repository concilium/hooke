from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from . import HookeModelBase

# session engine for SQLite in-memory database

@event.listens_for( Engine, 'connect' )
def set_sqlite_foreign_keys_pragma( dbapi_connection, connection_record ):
    cursor = dbapi_connection.cursor()
    cursor.execute( 'PRAGMA foreign_keys=ON' )
    cursor.close()
    
engine = create_engine( 'sqlite:///:memory:' )
HookeModelBase.metadata.create_all( engine )

SQLiteMemorySession = sessionmaker( bind = engine )






