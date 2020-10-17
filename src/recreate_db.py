from sqlalchemy import create_engine
from config import MYSQL_ROSPARK_DB
from db.rospark_db import Base, make_engine


try:
    engine = make_engine(MYSQL_ROSPARK_DB)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine,
                             tables=[Base.metadata.tables["parkings"]])
except Exception as e:
    print("Error: " + str(e))
