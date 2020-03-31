from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker

# setup db which runs on memory
# engine = create_engine('sqlite:///:memory:', echo=True)

#All model class which ORMapped must derive from Base
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50))
    password = Column(String(50))
    
    def init_user_table(self, engine):
        """
        Only run once for all time, except when the table has been deleted
        """
        self.metadata.create_all(engine)
        
    def get_account(self, session):
        user = session.query(User).filter(User.username=="admin").order_by(User.id).first()
        return user.username, user.password
    
    # internal debug method
    def __repr__(self):
        return "<User(username='%s', password='%s')>" % (
                             self.username, self.password)

