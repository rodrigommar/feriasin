# import library
from sqlalchemy import create_engine

# database
DATA_BASE = 'bd_user.sqlite'

# criando uma engine para conectar com um SQLite
engine = create_engine('sqlite:///{DATA_BASE}')

# conectando
connection = engine.connect()

# usando SQLAlchemy ORM
