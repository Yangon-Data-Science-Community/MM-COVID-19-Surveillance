import os
from sqlalchemy import create_engine

def clear_up(filename):
    """Delete the processed file>"""
    os.remove(filename)
    return True

# create sqlalchemy engine
def db_engine():
    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                        .format(user="root",
                                pw="wuthmone08",
                                db="Convid19"))
    return engine

def db_engine_close(engine):
    engine.dispose()
    return True