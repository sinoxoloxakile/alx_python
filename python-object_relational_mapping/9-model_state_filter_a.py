from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)
    username, password, db_name = sys.argv[1:]
    engine = create_engine('mysql+pymysql://{}:{}@localhost:3306/{}'.format(username, password, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.contains('a')).order_by(State.id.asc())
    for state in states:
        print(state.id, state.name)