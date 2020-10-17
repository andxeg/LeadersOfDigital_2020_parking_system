import pbjson
import datetime
from sqlalchemy import Column, String, Integer, REAL, DateTime
from sqlalchemy import Index, create_engine
from sqlalchemy.dialects.mysql import LONGBLOB
from sqlalchemy.ext import mutable
from sqlalchemy.types import TypeDecorator
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import scoped_session, sessionmaker


Base = declarative_base()

# https://www.michaelcho.me/article/json-field-type-in-sqlalchemy-flask-python
class JsonEncodedDict(TypeDecorator):
    """Enables JSON storage by encoding and decoding on the fly."""
    impl = LONGBLOB

    def process_bind_param(self, value, dialect):
        if value is None:
            return '{}'
        else:
            return pbjson.dumps(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return {}
        else:
            return pbjson.loads(value)


mutable.MutableDict.associate_with(JsonEncodedDict)

class ParkingsRecordsTbl(Base):
    __tablename__ = 'parkings'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    longitude = Column(REAL)
    latitude  = Column(REAL)
    total     = Column(REAL)
    free      = Column(REAL)
    photo     = Column(LONGBLOB)

    def _asdict(self):
        return dict([(k, v) for k, v in vars(self).items() if not k.startswith('_')])

    def serialize(self):
        return {
            # "created_date": str(self.created_date),
            "coordinate": {
                "longitude": float(self.longitude),
                "latitude": float(self.latitude)
            },
            "total": int(self.total),
            "free": int(self.free),
            # "photo": str(self.photo)
        }


def make_engine(mysql_db):
    return create_engine(
                mysql_db,
                encoding='utf8', pool_recycle=600, pool_pre_ping=True,
                connect_args={'connect_timeout': 1} if mysql_db.startswith("mysql://") else None
            )

def make_session_context(app, name, mysql_db):
    engine = make_engine(mysql_db)
    session = scoped_session(sessionmaker(bind=engine))
    app.context[name] = session
    
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        session.remove()
