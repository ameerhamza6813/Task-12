from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_config = {
    'user': 'Hamza',
    'password': 'Hamza.1234',
    'host': 'todo-api.chik60c2yq93.eu-north-1.rds.amazonaws.com',
    'port': 5432,
    'database': 'todoapi'
}


db_url = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
engine = create_engine(db_url)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
