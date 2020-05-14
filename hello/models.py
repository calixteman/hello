from datetime import datetime
from . import db, app


class Log(db.Model):
    __tablename__ = "log"

    key = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime(timezone=True), primary_key=True)

    def __init__(self):
        self.time = datetime.now()

    @staticmethod
    def add_entry():
        db.session.add(Log())
        db.session.commit()

    @staticmethod
    def get_entries():
        return db.session.query(Log.time).order_by(Log.key.asc())


def clear():
    db.session.close()
    db.drop_all()
    db.session.commit()


def create():
    engine = db.get_engine(app)
    if not engine.dialect.has_table(engine, "log"):
        db.create_all()
